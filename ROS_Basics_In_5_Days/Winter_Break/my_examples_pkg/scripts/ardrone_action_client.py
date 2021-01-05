#! /usr/bin/env python

import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

nImage = 1

# called wehn feedback is received from action server
def feedback_callback(feedback):
    global nImage
    # prints message indicating a new message has been received
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# initialize action client node
rospy.init_node("drone_action_client")

# create connection to action server
client = actionlib.SimpleActionClient("/ardrone_action_server", ArdroneAction)
# waits until action server is up and running
client.wait_for_server()

# create a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10

# sends goal to action server, specifying which feedback function to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

time.sleep(3)
client.cancel_goal() # would cancel goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
status = client.get_state()

client.wait_for_result()

print("[Result] State: %d"%(client.get_state()))