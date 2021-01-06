#! /usr/bin/env python

import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

# We create some constants with the corresponing vaules from the SimpleGoalState class
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1

def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

def fly_my_drone(lin_x=0, lin_y=0, lin_z=0, ang_z=0):
    # linear x controls forward (+1) and backword (-1)
    # linear y controls left (+1) and right (-1)
    # linear z controls up (+1) and down (-1)
    fly.linear.x = lin_x
    fly.linear.y = lin_y
    fly.linear.z = lin_z
    # angular z controls CCV(+1) and CV (-1)
    fly.angular.z = ang_z
    rospy.sleep(1)
    pub.publish(fly)
    rospy.loginfo("Flying")

# initializes the action client node
rospy.init_node('node_drone_action_client')

# publisher for Twist
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
fly = Twist()

# publisher for takeoff
takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
while takeoff.get_num_connections() < 1:
    rospy.sleep(1)

# publisher for land
land = rospy.Publisher('/drone/land', Empty, queue_size=1)
while land.get_num_connections() < 1:
    rospy.sleep(1)

# action server
action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name, ArdroneAction)

# waits until the action server is up and running
rospy.loginfo('Waiting for action Server '+action_server_name)
client.wait_for_server()
rospy.loginfo('Action Server Found...'+action_server_name)

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10 # indicates, take pictures along 10 seconds

client.send_goal(goal, feedback_cb=feedback_callback)

state_result = client.get_state()

rate = rospy.Rate(1)

rospy.loginfo("state_result: "+str(state_result))

takeoff.publish(Empty()) # takeoff publishing
rospy.loginfo("Taking off...")

while state_result < DONE:
    
    fly_my_drone(lin_x=-1, lin_y=0, lin_z=0, ang_z=0)
    fly_my_drone(lin_x=0, lin_y=0, lin_z=0, ang_z=1)
    fly_my_drone(lin_x=0, lin_y=1, lin_z=0, ang_z=0)
    fly_my_drone(lin_x=-1, lin_y=0, lin_z=0, ang_z=0)

    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))

if state_result > DONE:
    land.publish(Empty()) # land publishing
    rospy.loginfo("Landing...")
    
rospy.loginfo("[Result] State: "+str(state_result))
if state_result == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
    rospy.logwarn("There is a warning in the Server Side")

# rospy.loginfo("[Result] State: "+str(client.get_result()))