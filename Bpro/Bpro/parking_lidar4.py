import rclpy, sys, os
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

class SubLaser(Node):
    def __init__(self):
        super().__init__('sub_laser')
        
        self.sub_scan = self.create_subscription(
           LaserScan,           
            '/scan',       
            self.get_scan,   
            qos_profile_sensor_data)
        self.scan = LaserScan()
        
        
    def get_scan(self, msg):
        self.scan = msg
      
        
def main(args=None):
    print("strart lidar")
    rclpy.init(args=args)
    node = SubLaser()
    
    try:
         while rclpy.ok():
            rclpy.spin_once(node, timeout_sec = 0.1)
            if len(node.scan.ranges) != 360:
                pass
            else:
                if node.scan.ranges[270] > 1.1:
                    print("Parking Lot A4: Empty")
                    print("-----------------------------")
                    os.system("ros2 param set /reg_params z4_state 가능")
                    print("go to position5")
                    os.system("ros2 run Bpro parking_lot5")
                    sys.exit(1)
                else:
                    print("Parking Lot A4: Busy")
                    os.system("ros2 param set /reg_params z4_state 불가")
                    os.system("ros2 run Bpro parking_marker4 4")
                    sys.exit(1)
                    
                    
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()

