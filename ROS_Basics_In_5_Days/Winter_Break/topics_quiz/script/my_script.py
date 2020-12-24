#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node("topics_quiz_node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback)

rospy.spin()