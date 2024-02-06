import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import math
import pyrealsense2 as rs
import statistics
from std_msgs.msg import String
from ultralytics import YOLO
import matplotlib.pyplot as plt

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
        self.pub_x = self.node.create_publisher(String, 'x_coordinate', 10)
        self.pub_y = self.node.create_publisher(String, 'y_coordinate', 10)
        self.pub_z = self.node.create_publisher(String, 'z_coordinate', 10)
        self.pub_n_x = self.node.create_publisher(String, 'n_x', 10)
        self.pub_n_y = self.node.create_publisher(String, 'n_y', 10)
        self.pub_n_z = self.node.create_publisher(String, 'n_z', 10)
        self.model = YOLO('/home/jitesh/flipkart_ws/src/my_cam_scripts/my_cam_scripts/best.pt')

    def image_callback(self, msg):
        try:
            # Convert the ROS Image message to a CV2 image with 16UC1 encoding
            self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='16UC1')
            # Apply a colormap to the depth image for visualization
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image, alpha=0.03), cv2.COLORMAP_JET)
            #print(depth_image)
            # Display the depth image (you can perform other operations here)
            #cv2.imshow('Depth Image', self.depth_image)
            #cv2.waitKey(1)

            '''# Convert the ROS Image message to a CV2 image with BGR8 encoding
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Display the image (you can perform other operations here)
            cv2.imshow('RealSense Image', cv_image)
            cv2.waitKey(1)'''

        except Exception as e:
            print(e)

    def color_callback(self, msg):
        try:
            self.color_frame_recieved = self.bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')
            color_frame = self.color_frame_recieved
            depth_image = self.depth_image
            color_frame = cv2.resize(color_frame, (depth_image.shape[1], depth_image.shape[0]))
            results = self.model(color_frame, save=True, show=False)
            self.z=[]
            self.n=[]
            self.o=[]
            p=[]
            q=[]
            for r in results:
                a=r.masks.xy[0]
                self.length=len(a)
                #print(length)
                l = r.masks.xy[0][:,0]
                m = r.masks.xy[0][:,1]   
                max_x = np.amax(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
                max_y = np.amax(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
                min_x = np.amin(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
                min_y = np.amin(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
                y_min_x  =find_y_for_x(min_x, a)
                y_max_x  =find_y_for_x(max_x, a)
                x_min_y =find_x_for_y(min_y,a)
                x_max_y =find_x_for_y(max_y,a)
                x2= (min_x+max_x)/2
                y2= (min_y+max_y)/2
                pointc = [int(x2),int(y2)]
                point5=[int(x_min_y),int(min_y)]
                point6=[int(x_max_y),int(max_y)]
                point7= [int(min_x),int(y_min_x)]
                point8=[int(max_x),int(y_max_x)]
                point9=[int((3*x_max_y+x2)/4),int((3*max_y+y2)/4)]
                point10= [int((3*min_x+x2)/4),int((3*y_min_x+y2)/4)]
                
                for i in range(len(l)):
                    self.n.append(int((3*(int(l[i]))+pointc[0])/4))
                    self.o.append(int((3*(int(m[i]))+pointc[1])/4))
                print(self.n)
                print(self.o)
                for i in range(len(l)):
                    p.append(int((3*(int(l[i]))+pointc[0])*90/1488))
                    q.append(int((3*(int(m[i]))+pointc[1])*60/1000))
                print(p)
                print(q)
                x = p
                y = q
                cv2.circle(color_frame,pointc,4,(0,0,255))
                cv2.line(color_frame, point7, point8, (255, 0, 255), 2)
                cv2.line(color_frame, point5, point6, (55, 167, 25), 2)
                cv2.line(color_frame, point9, point10, (0,0,0),2)

            max_x = np.amax(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
            max_y = np.amax(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
            min_x = np.amin(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
            min_y = np.amin(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
            self.x2= (min_x+max_x)/2
            self.y2= (min_y+max_y)/2
            s = x2*(90/372)
            t = y2*(60/250)
            s_str = String()
            t_str = String()
            s_str.data = str(s)
            t_str.data = str(t)
            self.pub_x.publish(s_str)
            self.pub_y.publish(t_str)
            print("centre_x",x2*(90/372))
            print("centre_y",y2*(60/250))
            depthofz = self.vishal(depth_image, color_frame)
            my_array = self.z
            meanz = self.mean_of_non_zero(my_array)
            print("centre_mean",meanz)
            z_str = String()
            z_str.data = str(meanz)
            self.pub_z.publish(z_str)

            array_3d = np.column_stack((x, y, self.z))
            print(array_3d)
            coordinates = array_3d

            # Extract x, y, and z coordinates
            x, y, z = coordinates[:, 0], coordinates[:, 1], coordinates[:, 2]

            fig = plt.figure(0)
            ax = plt.axes(projection='3d')
            ax.plot3D(x,y,z,".")


            # Set axis labels
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            A=np.ones((len(x),3))
            A[:,0]=x
            A[:,1]=y

            X=np.linalg.inv(A.transpose() @ A) @ A.transpose() @ z
            print(X)

            plane=X[0]*x+X[1]*y+ X[2]
            n_x = String()
            n_x.data = str(X[0])
            self.pub_n_x.publish(n_x)
            n_y = String()
            n_y.data = str(X[1])
            self.pub_n_y.publish(n_y)
            n_z = String()
            n_z.data = str(X[2])
            self.pub_n_z.publish(n_z)

            '''fig=plt.figure(1)
            ax=plt.axes(projection='3d')
            ax.plot_trisurf(x,y,plane)'''

            cv2.imshow("centre",color_frame)
            cv2.imshow("depth",depth_image)
            #plt.show()
            #cv2.imshow('Color Image', color_frame)
            cv2.waitKey(1)
        except Exception as e:
            print(e)


    def find_depth_at_point(self, depth_frame, x, y):
        try:
            # Convert x, y to integers
            x = int(x)
            y = int(y)

            # Access depth value at (y, x) in the depth frame
            depth_value = depth_frame[y, x]

            print(f"Depth at ({x}, {y}): {depth_value}")
            return depth_value
        except Exception as e:
            print(f"Error in find_depth_at_point: {e}")
            return None
        
    def mean_of_non_zero(self, array):
        non_zero_sum = 0
        non_zero_count = 0

        for value in array:
            if value != 0:
                non_zero_sum += value
                non_zero_count += 1

        # Avoid division by zero
        if non_zero_count != 0:
            mean = non_zero_sum / non_zero_count
            return mean
        else:
            return None
    def vishal(self, depth_frame, color_frame):
        depth_image = depth_frame
        #color_image = np.asanyarray(color_frame.get_data())
        depthofz = depth_image[int(self.y2), int(self.x2)]
        print("height of centre",depthofz)
        for i in range(self.length):
            x1,y1 = (self.n[i],self.o[i])
            distance = depth_image[y1, x1]
            self.z.append(distance)
        return depthofz

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
