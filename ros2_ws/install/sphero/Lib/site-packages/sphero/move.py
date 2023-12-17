
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from spherov2.toy.mini import Mini
from spherov2.types import Color
from spherov2 import scanner
from . import spheroapi as SpheroEduAPI

class SpheroSubscriberNode(Node):
    def __init__(self):
        super().__init__('sphero_subscriber_node')
        self.subscription = self.create_subscription(
            String, 'serial_data_topic', self.listener_callback, 10)
        self.get_logger().info('Subscriber node initialized and listening on serial_data_topic')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received message: {msg.data}')
        if msg.data == "NEC Data: E31CFF00":
            self.get_logger().info('Trigger found, executing control logic')
            self.control_sphero()
        else:
            self.get_logger().info('Received data does not match trigger')

    def control_sphero(self):
        toy = scanner.find_Mini()
        if toy is None:
            self.get_logger().info('Sphero not found')
            return
        self.get_logger().info('Sphero found, executing commands')
        with SpheroEduAPI.SpheroEduAPI(toy) as droid:
            droid.set_speed(120)
            droid.set_heading(90)
            self.get_logger().info('Commands executed on Sphero')

def main(args=None):
    rclpy.init(args=args)
    node = SpheroSubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()