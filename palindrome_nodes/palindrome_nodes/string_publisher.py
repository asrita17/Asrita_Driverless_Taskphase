import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String

def main(args=None):
    rclpy.init(args=args)
    node = Node('string_publisher')
    publisher = node.create_publisher(RT2String, '/input_string', 10)
    print("Enter strings to check. Press Ctrl+C to stop.")

    try:
        while rclpy.ok():
            text = input("Enter a string: ")
            msg = RT2String()
            msg.data = text
            publisher.publish(msg)
            node.get_logger().info(f'Published: {text}')
            rclpy.spin_once(node, timeout_sec=0.1)
    except (KeyboardInterrupt, EOFError):
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
