#! /usr/bin/env python

import rospy
import actionlib
from turtlebot_maze.msg import MyTurtlebotMazeActionFeedback, MyTurtlebotMazeActionAction, MyTurtlebotMazeActionResult, MyTurtlebotMazeActionGoal
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan 
from time import sleep
from std_srvs.srv import Trigger, TriggerRequest
from std_msgs.msg import Empty

rospy.init_node("node_turtlebot_maze_project_client")

# action client
def feedback_callback(feedback):
    pass 

client = actionlib.SimpleActionClient("/turtlebot_maze_action_server", MyTurtlebotMazeActionAction)
client.wait_for_server()

goal = MyTurtlebotMazeActionGoal()
client.send_goal(goal, feedback_cb=feedback_callback)

sleep(2)

# service client
rospy.wait_for_service("/turtlebot_maze_service_server")
my_turtlebot_service = rospy.ServiceProxy("/turtlebot_maze_service_server", Trigger)
my_turtlebot_service_object = TriggerRequest()
result = my_turtlebot_service(my_turtlebot_service_object)
print result 

client.wait_for_result()
action_result = client.get_result()
print("Last Pose:")
print action_result.result_odom_array[-1]