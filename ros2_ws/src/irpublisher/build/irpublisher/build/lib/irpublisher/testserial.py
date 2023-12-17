import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialPublisherNode(Node):
    def __init__(self):
        super().__init__('serial_publisher_node')
        self.ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your serial port name
        self.publisher = self.create_publisher(String, 'serial_data', 10)
        timer_period = 0.1  # 0.1 seconds
        self.timer = self.create_timer(timer_period, self.publish_serial_data)

    def publish_serial_data(self):
        try:
            line = self.ser.readline()
            decoded_line = line.decode('utf-8').strip()
            msg = String()
            msg.data = decoded_line
            self.publisher.publish(msg)
        except KeyboardInterrupt:
            self.get_logger().info("Serial communication stopped by user.")
            self.ser.close()

def main(args=None):
    rclpy.init(args=args)
    serial_publisher = SerialPublisherNode()
    rclpy.spin(serial_publisher)
    serial_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
