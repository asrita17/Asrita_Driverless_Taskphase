import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ResultProcessor(Node):
    def __init__(self):
        super().__init__('result_processor')
        self.publisher = self.create_publisher(String, '/palindrome_response', 10)
        self.subscription = self.create_subscription(
            Int32, '/palindrome_result', self.process_result, 10
        )

    def process_result(self, msg):
        response = String()
        response.data = 'Yes' if msg.data == 1 else 'No'
        self.publisher.publish(response)
        self.get_logger().info(f'Sent response: {response.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ResultProcessor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
