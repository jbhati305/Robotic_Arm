import rclpy
from std_msgs.msg import Float32MultiArray

def publish_xyz(x, y, z):
    msg = Float32MultiArray()
    msg.data = [x, y, z]
    publisher.publish(msg)

def get_xyz_input():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    return x, y, z

def main(args=None):
    rclpy.init(args=args)

    global publisher
    node = rclpy.create_node('xyz_publisher_node')
    publisher = node.create_publisher(Float32MultiArray, 'xyz_topic', 10)

    while rclpy.ok():
        x, y, z = get_xyz_input()
        publish_xyz(x, y, z)
        
        # Replace node.spin_once() with rclpy.spin_once(node)
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
