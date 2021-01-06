#! /usr/bin/env python

import rospy
import time
import actionlib
from actionlib.msg import TestFeedback, TestResult, TestAction, TestGoal

def feedback_callback(feedback):
    rospy.loginfo("feedback => %d" %feedback.feedback)

rospy.init_node("node_drone_square_action_client")
client = actionlib.SimpleActionClient("/drone_square_as", TestAction)
client.wait_for_server()

goal = TestGoal()
goal.goal = 5
client.send_goal(goal, feedback_cb = feedback_callback)
time.sleep(3)
# client.cancel_goal()
status = client.get_state()
i = 0
rospy.loginfo("Status => %d" %status)
while status < 2:
    # do something else
    status = client.get_state()
    
rospy.loginfo("Status => %d" %status)
rospy.loginfo("Completed from client")