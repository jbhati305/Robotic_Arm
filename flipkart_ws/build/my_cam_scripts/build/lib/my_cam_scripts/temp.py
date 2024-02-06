import numpy as np
from ultralytics import YOLO
import cv2
import pyrealsense2 as rs
from realsense_depth import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
dc=DepthCamera()
ret,depth_frame,color_frame =dc.get_frame()
z=[]
n=[]
o=[]
p=[]
q=[]
model = YOLO('best (7).pt')

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
results = model(color_frame,save=True,show=True)
for r in results:
    a=r.masks.xy[0]
    length=len(a)
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
        n.append(int((3*(int(l[i]))+pointc[0])/4))
        o.append(int((3*(int(m[i]))+pointc[1])/4))
    print(n)
    print(o)
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
def centre_x_y():
    max_x = np.amax(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
    max_y = np.amax(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
    min_x = np.amin(r.masks.xy[0][:, 0])  # Maximum along the first column (x values)
    min_y = np.amin(r.masks.xy[0][:, 1])  # Maximum along the second column (y values)
    x2= (min_x+max_x)/2
    y2= (min_y+max_y)/2
    s = x2*(90/372)
    t = y2*(60/250)
    print("centre_x",x2*(90/372))
    print("centre_y",y2*(60/250))
    return s,t
def vishal():
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
    frames = pipeline.wait_for_frames()
            # Align the depth frame to the color frame
    aligned_frames = align.process(frames)
    depth_frame = aligned_frames.get_depth_frame()
    color_frame = aligned_frames.get_color_frame()
    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    depthofz = depth_image[int(y2), int(x2)]
    print("height of centre",940-depthofz)
    for i in range(length):
        x1,y1 = (n[i],o[i])
        distance = depth_image[y1, x1]
        z.append(940 -distance)
    
    pipeline.stop()
    return depthofz
#print(z)
def mean_of_non_zero(array):
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
        return None  # Handle the case when there are no non-zero values in the array

my_array = z
meanz = mean_of_non_zero(my_array)
print("centre_mean",meanz)

array_3d = np.column_stack((x, y, z))
print(array_3d)
# Your 3D coordinates
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

fig=plt.figure(1)
ax=plt.axes(projection='3d')
ax.plot_trisurf(x,y,plane)

cv2.imshow("centre",color_frame)
cv2.imshow("depth",depth_frame)
plt.show()