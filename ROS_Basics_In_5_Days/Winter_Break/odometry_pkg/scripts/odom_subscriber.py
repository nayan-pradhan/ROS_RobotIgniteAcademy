#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print msg

rospy.init_node("node_odom_subscriber")
sub = rospy.Subscriber("/odom", Odometry, callback)
rospy.spin()