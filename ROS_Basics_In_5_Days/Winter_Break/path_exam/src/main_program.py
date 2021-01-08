#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_srvs.srv import Trigger, TriggerRequest
from geometry_msgs.msg import Twist, Pose
import actionlib
from path_exam.msg import RecordOdomAction, RecordOdomFeedback, RecordOdomResult, RecordOdomGoal
import time

rospy.init_node("node_main_program")

# service client
rospy.wait_for_service("/my_service")
my_service_service = rospy.ServiceProxy("/my_service", Trigger)
my_service_object = TriggerRequest()
result = my_service_service(my_service_object)
print result

# action client
def feedback_callback(feedback):
    pass

client = actionlib.SimpleActionClient("rec_pose_as", RecordOdomAction)
client.wait_for_server()

goal = RecordOdomGoal()

client.send_goal(goal, feedback_cb=feedback_callback)

client.wait_for_result()
action_result = client.get_result()
print("Last Pose:")
print action_result.result_list[-1]