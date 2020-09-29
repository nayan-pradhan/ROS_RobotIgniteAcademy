#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def call_back(msg):
    print (msg)
    return

rospy.init_node('odometry_subscriber')
sub = rospy.Subscriber('/odom', Odometry, call_back)
rospy.spin()