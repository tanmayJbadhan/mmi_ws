import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialPublisherNode(Node):
    def __init__(self):
        super().__init__('serial_publisher_node')
        self.ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your serial port name
        self.publisher = self.create_publisher(String, 'serial_data_topic', 10)
        timer_period = 0.1  # Frequency of publishing data in seconds
        self.timer = self.create_timer(timer_period, self.publish_serial_data)

    def publish_serial_data(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline()
            decoded_line = line.decode('utf-8').strip()
            msg = String()
            msg.data = decoded_line
            self.publisher.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    serial_publisher_node = SerialPublisherNode()
    rclpy.spin(serial_publisher_node)
    serial_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
