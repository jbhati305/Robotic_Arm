import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import math
import pyrealsense2 as rs
import statistics
from ultralytics import YOLO

class RealSenseImageSubscriber:
    def __init__(self):
        self.node = rclpy.create_node('realsense_image_subscriber')
        self.bridge = CvBridge()
        self.image_sub = self.node.create_subscription(
            Image,
            '/camera/depth/image_rect_raw',
            self.image_callback,
            10  # QoS profile
        )
        self.color_sub = self.node.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.color_callback,
            10
        )
        self.pipeline = None  # Initialize the pipeline

    def image_callback(self, msg):
        try:
            # Convert the ROS Image message to a CV2 image with 16UC1 encoding
            self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='16UC1')
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image, alpha=0.03), cv2.COLORMAP_JET)
            cv2.imshow('Depth Image', depth_colormap)
            cv2.waitKey(1)

            # Convert the ROS Image message to a CV2 image with BGR8 encoding
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            cv2.imshow('RealSense Image', cv_image)
            cv2.waitKey(1)

        except Exception as e:
            print(f"Error in image_callback: {e}")

    def color_callback(self, msg):
        try:
            if self.model is None:
                self.model = YOLO('best (7).pt')

            a = []
            color_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')
            color_frame = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color Image', color_image)
            results = self.model(color_frame, save=True, show=True)

            for r in results:
                #print(r.masks.xy[0].max([:,0]))  # print the Masks object containing the detected instance masks
                #pairs_array = r.masks.xy[0]
                data = r.masks.xy[0]
                max_x = np.amax(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
                max_y = np.amax(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
                min_x = np.amin(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
                min_y = np.amin(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
                y_min_x  =find_y_for_x(min_x, data)
                y_max_x  =find_y_for_x(max_x, data)
                x_min_y =find_x_for_y(min_y,data)
                x_max_y =find_x_for_y(max_y,data)
                x= (min_x+max_x)/2
                y= (min_y+max_y)/2
                point = [int(x),int(y)]
                x1= (x + min_x)/2
                x2=(x + max_x)/2
                y1= (y + min_y)/2
                y2=(y + max_y)/2
                point1=[int(x),int(y1)]
                point2=[int(x),int(y2)]
                point3=[int(x1),int(y)]
                point4=[int(x2),int(y)]
                point5=[int(x_min_y),int(min_y)]
                point6=[int(x_max_y),int(max_y)]
                point7= [int(min_x),int(y_min_x)]
                point8=[int(max_x),int(y_max_x)]
                diagonal_angle_1 = math.degrees(math.atan((max_y-min_y)/(x_max_y-x_min_y)))
                print("diagonal_angle_1", diagonal_angle_1)  
                diagonal_angle_2 = math.degrees(math.atan((y_max_x-y_min_x)/(max_x-min_x)))
                print("diagonal_angle_2", diagonal_angle_2)

            # Initialize pipeline if not done already
            if self.pipeline is None:
                self.initialize_pipeline()

            # Process frames using the pipeline
            self.process_frames(50, point, a)

        except Exception as e:
            print(f"Error in color_callback: {e}")

    def initialize_pipeline(self):
        # Create a pipeline
        self.pipeline = rs.pipeline()

        # Create a config object
        config = rs.config()

        # Enable depth stream
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(config)
        self.align = rs.align(rs.stream.color)

    def process_frames(self, num_frames, point, depth_values):
        for i in range(num_frames):
            frames = self.pipeline.wait_for_frames()
            aligned_frames = self.align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()

            if not depth_frame:
                continue

            depth_image = np.asanyarray(depth_frame.get_data())
            distance = depth_image[point[1], point[0]]
            depth_values.append(distance)
            print(f"Frame {i + 1}: Depth at point ({point[0]}, {point[1]}): {distance} meters")

        print(depth_values)
        print(statistics.mode(depth_values))

def find_depth_at_point(depth_frame, x, y):
    depth_value = depth_frame.get_distance(x, y)
    return depth_value

def find_y_for_x(x_value, data):
    for x, y in data:
        if x == x_value:
            return y
    return None

def find_x_for_y(y_value, data):
    for x, y in data:
        if y == y_value:
            return x
    return None

def main():
    rclpy.init()
    rs_image_subscriber = RealSenseImageSubscriber()
    rclpy.spin(rs_image_subscriber.node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
