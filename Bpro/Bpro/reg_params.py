import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType

class RegParams(Node):
    def __init__(self):
        super().__init__('reg_params')
        qos_profile = QoSProfile(depth=10)

        self.declare_parameter('z1_state', 'empty')
        self.declare_parameter('z2_state', 'empty')
        self.declare_parameter('z3_state', 'empty')
        self.declare_parameter('z4_state', 'empty')
        self.declare_parameter('z5_state', 'empty')
        self.declare_parameter('z6_state', 'empty')
        self.declare_parameter('z1_plate', '')
        self.declare_parameter('z2_plate', '')
        self.declare_parameter('z3_plate', '')
        self.declare_parameter('z4_plate', '')
        self.declare_parameter('z5_plate', '')
        self.declare_parameter('z6_plate', '')

def main():
    rclpy.init()
    node = RegParams()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
