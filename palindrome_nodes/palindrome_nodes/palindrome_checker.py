import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String
from std_msgs.msg import Int32, String

class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')
        self.publisher = self.create_publisher(Int32, '/palindrome_result', 10)
        self.subscription = self.create_subscription(
            RT2String, '/input_string', self.check_string, 10
        )
        self.response_subscription = self.create_subscription(
            String, '/palindrome_response', self.show_response, 10
        )

    def check_string(self, msg):
        text = msg.data
        result = Int32()
        result.data = int(text.lower().replace(' ', '') == text.lower().replace(' ', '')[::-1])
        self.publisher.publish(result)
        self.get_logger().info(f'Checking "{text}" -> {result.data}')

    def show_response(self, msg):
        self.get_logger().info(f'Response from Node 3: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
