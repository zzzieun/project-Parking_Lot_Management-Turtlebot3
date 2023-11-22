import rclpy, sys,os
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped 
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped, Quaternion

class ClientFollowPoints(Node):

    def __init__(self):
        super().__init__('client_follow_points')
        self._client = ActionClient(self, FollowWaypoints, '/FollowWaypoints')

    def send_points(self, points):
        msg = FollowWaypoints.Goal()
        msg.poses = points

        self._client.wait_for_server()
        self._send_goal_future = self._client.send_goal_async(msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        
        if status == GoalStatus.STATUS_SUCCEEDED:
            print("-----------------------------")
            print("arrived at goal position1!!!!!")
            os.system("ros2 run Bpro parking_lidar1")
            sys.exit(1)
        
        self.get_logger().info('Result: {0}'.format(result.missed_waypoints))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.current_waypoint))

def main(args=None):	
    rclpy.init(args=args)

    node = ClientFollowPoints()
    #print('go waypoint1')

    rgoal = PoseStamped()
    rgoal.header.frame_id = "map"
    rgoal.header.stamp.sec = 0
    rgoal.header.stamp.nanosec = 0
    rgoal.pose.position.z = 0.0
    rgoal.pose.position.x = 1.1
    rgoal.pose.position.y = -0.10879
    rgoal.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.7071067811865476, w=0.7071067811865476)
    print(rgoal)
    mgoal = [rgoal]
    
    node.send_points(mgoal)

    rclpy.spin(node)
