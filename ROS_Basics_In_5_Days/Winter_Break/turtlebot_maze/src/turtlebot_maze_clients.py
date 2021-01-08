#! /usr/bin/env python

import rospy
import actionlib
from turtlebot_maze.msg import MyTurtlebotMazeActionFeedback, MyTurtlebotMazeActionAction, MyTurtlebotMazeActionResult, MyTurtlebotMazeActionGoal
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan 
from time import sleep
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest

# inti node
rospy.init_node("node_turtlebot_clients")

## service client
rospy.wait_for_service("/turtlebot_maze_service_server")
my_service = rospy.ServiceProxy("/turtlebot_maze_service_server", Trigger)

# my_service_object = TriggerRequest()
# result = my_service(my_service_object)
# print(result)

## action client
def feedback_callback(feedback):
    rospy.loginfo("feedback => %d" %feedback.feedback)

client = actionlib.SimpleActionClient("/turtlebot_maze_action_server", MyTurtlebotMazeActionAction)
client.wait_for_server()

# goal = MyTurtlebotMazeActionGoal()
# time.sleep(3)
# client.cancel_goal()
# status = client.get_state()
# i = 0
# rospy.loginfo("Status => %d" %status)
# while status < 2:
#     # do something else
#     status = client.get_state()
    
# rospy.loginfo("Status => %d" %status)