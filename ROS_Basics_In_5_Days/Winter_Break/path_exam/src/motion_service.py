#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty as Empty
from std_srvs.srv import Empty as Empty_srv
from std_srvs.srv import EmptyResponse as Empty_srv_response
from geometry_msgs.msg import Twist
import time

###

def callback(request):
    response = Empty_srv_response()

    takeoff_func()
    move_forward_func()
    rospy.sleep(5)
    stop_func()
    land_func()

    return response

### 

def takeoff_func():
    rospy.loginfo("Taking off ...")
    pub_takeoff.publish(Empty())
    rospy.sleep(1)
    rospy.loginfo("Took off!")

def land_func():
    rospy.loginfo("Landing ...")
    pub_land.publish(Empty())
    rospy.sleep(1)
    rospy.loginfo("Landed!")

def move_forward_func():
    rospy.loginfo("Moving forward ...")
    # linear x controls forward (+1) and backword (-1)
    # linear y controls left (+1) and right (-1)
    # linear z controls up (+1) and down (-1)
    move.linear.x = 0.5
    move.linear.y = 0
    move.linear.z = 0
    # angular z controls CCV(+1) and CV (-1)
    move.angular.z = 0
    rospy.loginfo("Moved forward!")
    pub_move.publish(move)

def stop_func():
    rospy.loginfo("Stopping ...")
    # linear x controls forward (+1) and backword (-1)
    # linear y controls left (+1) and right (-1)
    # linear z controls up (+1) and down (-1)
    move.linear.x = 0
    move.linear.y = 0
    move.linear.z = 0
    # angular z controls CCV(+1) and CV (-1)
    move.angular.z = 0
    rospy.sleep(2)
    rospy.loginfo("Stopped!")
    pub_move.publish(move)

###

rospy.init_node("node_motion_service")

my_serv = rospy.Service("my_service", Empty_srv, callback)

pub_takeoff = rospy.Publisher("/drone/takeoff", Empty, queue_size=1)
while pub_takeoff.get_num_connections() < 1:
    rospy.sleep(1)

pub_move = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
while pub_move.get_num_connections() < 1:
    rospy.sleep(1)
move = Twist()

pub_land = rospy.Publisher("/drone/land", Empty, queue_size=1)
while pub_land.get_num_connections() < 1:
    rospy.sleep(1)

rospy.spin()