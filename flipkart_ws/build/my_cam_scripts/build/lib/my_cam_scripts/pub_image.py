import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import pyrealsense2 as rs
import numpy as np
import cv2
from time import sleep

class RealSenseDepthPublisher(Node):
    def __init__(self):
        super().__init__('realsense_depth_publisher')
        self.publisher_depth = self.create_publisher(Image, '/camera/depth/image_rect_raw', 10)
        self.publisher_color = self.create_publisher(Image, '/camera/color/image_raw', 10)
        self.bridge = CvBridge()

        # Configure RealSense pipeline for depth and color streams
        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)

        # Start streaming
        self.pipeline.start(config)

        self.timer = self.create_timer(10, self.timer_callback)

    def timer_callback(self):
        # Wait for the next set of frames from the camera
        frames = self.pipeline.wait_for_frames()

        # Get the depth and color frames
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            return
        align = rs.align(rs.stream.color)
        aligned_frames = align.process(frames)
        depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        
        # Convert the RealSense frames to CV2 images
        

        # Convert the CV2 images to ROS Image messages
        ros_depth_image = self.bridge.cv2_to_imgmsg(depth_image, '16UC1')
        ros_color_image = self.bridge.cv2_to_imgmsg(color_image, 'rgb8')

        # Set the frame ID and timestamp
        ros_depth_image.header.stamp = self.get_clock().now().to_msg()
        ros_color_image.header.stamp = ros_depth_image.header.stamp
        ros_depth_image.header.frame_id = "depth_frame"
        ros_color_image.header.frame_id = "color_frame"

        # Publish the ROS Image messages
        self.publisher_depth.publish(ros_depth_image)
        self.publisher_color.publish(ros_color_image)

def main(args=None):
    rclpy.init(args=args)
    realsense_depth_publisher = RealSenseDepthPublisher()
    rclpy.spin(realsense_depth_publisher)
    realsense_depth_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
