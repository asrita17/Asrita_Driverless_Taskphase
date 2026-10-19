import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne

class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.publisher = self.create_publisher(TaskOne, '/taskone', 10)
        self.msg = TaskOne()
        self.msg.ang_vel = float(input("Enter angular velocity (rad/s): "))
        self.msg.radius = float(input("Enter wheel radius (m): "))
        self.timer = self.create_timer(0.5, self.publish_message)

    def publish_message(self):
        self.publisher.publish(self.msg)
        self.get_logger().info(
            f'Published ang_vel={self.msg.ang_vel}, radius={self.msg.radius}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
