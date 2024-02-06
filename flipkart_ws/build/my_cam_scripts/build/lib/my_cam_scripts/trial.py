import numpy as np
import math
from ultralytics import YOLO
import cv2
import pyrealsense2 as rs
from realsense_depth import*
import time
import statistics


dc=DepthCamera()
ret,depth_frame,color_frame =dc.get_frame()

model = YOLO('best (7).pt')
a=[]
a1=[]
a2=[]
a3=[]
a4=[]
results = model(color_frame,save=True,show=True)
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
def main():
    # Create a pipeline
    pipeline = rs.pipeline()

    # Create a config object
    config = rs.config()

    # Enable depth stream
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    # Start streaming
    pipeline.start(config)
    align = rs.align(rs.stream.color)
    i =0
    try:
        # Capture 50 frames
        for i in range(50):
            
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            # Align the depth frame to the color frame
            aligned_frames = align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()

            if not depth_frame:
                continue

            # Convert depth frame to numpy array
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Find depth at a specific point (e.g., center of the image)
            x, y = (point[0],point[1])
            #depth_at_point = find_depth_at_point(depth_frame, x, y)*1000
            distance = depth_image[point[1], point[0]]
            #cv2.putText(color_image, "{}mm".format(distance), (point[0], point[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)    
            a.append(distance)
            # Display the depth information
            print(f"Frame {i + 1}: Depth at point ({x}, {y}): {distance} meters")
        print (a)
        print(statistics.mode(a))
        #print(statistics.mean(a))
        i=0       
        # Capture 50 frames
        for i in range(50):
            
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            # Align the depth frame to the color frame
            aligned_frames = align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()

            if not depth_frame:
                continue

            # Convert depth frame to numpy array
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Find depth at a specific point (e.g., center of the image)
            x, y = (point1[0],point1[1])
            #depth_at_point = find_depth_at_point(depth_frame, x, y)*1000
            distance = depth_image[point1[1], point1[0]]
            #cv2.putText(color_image, "{}mm".format(distance), (point[0], point[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)    
            a1.append(distance)
            # Display the depth information
            print(f"Frame {i + 1}: Depth at point ({x}, {y}): {distance} meters")
        print (a1)
        print(statistics.mode(a1))
        #print(statistics.mean(a1))

        i=0
    
        # Capture 50 frames
        for i in range(50):
            
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            # Align the depth frame to the color frame
            aligned_frames = align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()

            if not depth_frame:
                continue

            # Convert depth frame to numpy array
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Find depth at a specific point (e.g., center of the image)
            x, y = (point2[0],point2[1])
            #depth_at_point = find_depth_at_point(depth_frame, x, y)*1000
            distance = depth_image[point2[1], point2[0]]
            #cv2.putText(color_image, "{}mm".format(distance), (point[0], point[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)    
            a2.append(distance)
            # Display the depth information
            print(f"Frame {i + 1}: Depth at point ({x}, {y}): {distance} meters")
        print (a2)
        print(statistics.mode(a2))
        #print(statistics.mean(a))
   
        i=0

        # Capture 50 frames
        for i in range(50):
            
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            # Align the depth frame to the color frame
            aligned_frames = align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()

            if not depth_frame:
                continue

            # Convert depth frame to numpy array
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Find depth at a specific point (e.g., center of the image)
            x, y = (point3[0],point3[1])
            #depth_at_point = find_depth_at_point(depth_frame, x, y)*1000
            distance = depth_image[point3[1], point3[0]]
            #cv2.putText(color_image, "{}mm".format(distance), (point[0], point[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)    
            a3.append(distance)
            # Display the depth information
            print(f"Frame {i + 1}: Depth at point ({x}, {y}): {distance} meters")
        print (a3)
        print(statistics.mode(a3))
        #print(statistics.mean(a))
    
        i=0   
  
        # Capture 50 frames
        for i in range(50):
            
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            # Align the depth frame to the color frame
            aligned_frames = align.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()

            if not depth_frame:
                continue

            # Convert depth frame to numpy array
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Find depth at a specific point (e.g., center of the image)
            x, y = (point4[0],point4[1])
            #depth_at_point = find_depth_at_point(depth_frame, x, y)*1000
            distance = depth_image[point4[1], point4[0]]
            #cv2.putText(color_image, "{}mm".format(distance), (point[0], point[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)    
            a4.append(distance)
            # Display the depth information
            print(f"Frame {i + 1}: Depth at point ({x}, {y}): {distance} meters")
        print (a4)
        print(statistics.mode(a4))
        #print(statistics.mean(a))        

    finally:
        # Stop streaming
        pipeline.stop()
    
    d = int(statistics.mode(a))
    d1 = int(statistics.mode(a1))
    d2 = int(statistics.mode(a2))   
    d3 = int(statistics.mode(a3))   
    d4 = int(statistics.mode(a4))    
    print("RED",d)
    print("BLUE",d1)
    print("GREEN",d2)
    print("WHITE",d3)
    print("YELLOW",d4)
    m1=abs(point3[0]-point4[0])*(90/372)
    dist1=abs(d3-d4)
    theta1=math.degrees(math.atan(dist1/m1))
    m2=abs(point1[1]-point2[1])*(60/250)
    dist2=abs(d1-d2)
    theta2=math.degrees(math.atan(dist2/m2))
    print("angle in x",theta1) 
    print("angle in y", theta2)
    #color_frame = np.asarray(color_frame)
# Convert color_frame to numpy array
    color_frame_np = np.asarray(color_frame)

# Draw lines on the numpy array

    cv2.imwrite('output_image.jpg',color_frame)
    print("Maximum value of x:", max_x)
    print("Maximum value of y:", max_y)
    print("Minimum value of x:", min_x)
    print("Minimum value of y:", min_y)
    print(x)
    print(y)

if __name__ == "__main__":
   main()
cv2.line(color_frame, point7, point8, (255, 0, 255), 2)
cv2.line(color_frame, point5, point6, (55, 167, 25), 2)
cv2.line(color_frame, point3, point4, (5, 167, 255), 2)
cv2.circle(color_frame,point,4,(0,0,255))
cv2.circle(color_frame,point1,4,(255,0,0))
cv2.circle(color_frame,point2,4,(0,255,0))
cv2.circle(color_frame,point3,4,(255,255,255))
cv2.circle(color_frame,point4,4,(0,255,255))
cv2.circle(color_frame,point5,4,(0,0,255))
cv2.circle(color_frame,point6,4,(0,0,255))
cv2.circle(color_frame,point7,4,(0,0,255))
cv2.circle(color_frame,point8,4,(0,0,255))
cv2.imshow("centre",color_frame)
cv2.imshow("depth",depth_frame)
cv2.waitKey(0)