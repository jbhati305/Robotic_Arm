import rclpy
from std_msgs.msg import Int32
from my_msg_package.msg import MyMessage

def main():
    rclpy.init()
    node = rclpy.create_node('my_publisher')
    publisher = node.create_publisher(MyMessage, 'my_topic', 10)

    msg = MyMessage()
    msg.data = 42  # Set your data

    while rclpy.ok():
        publisher.publish(msg)
        node.get_logger().info('Publishing: %d' % msg.data)
        rclpy.spin_once(node)

if __name__ == '__main__':
    main()