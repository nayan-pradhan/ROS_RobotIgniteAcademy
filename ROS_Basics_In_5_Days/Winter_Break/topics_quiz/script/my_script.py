#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node("topics_quiz_node") # initialize node

move = Twist() # creating twist object

lin_vel = 0.0
ang_vel = 0.4

def callback(msg):
	if msg.ranges[360] > 1: # if object to the front is more than a distance of 1
		move.linear.x = lin_vel
		move.angular.y = 0.0
	if msg.ranges[360] < 1: # if object to the front is at a distance smaller than 1
		move.linear.x = 0.0
		move.angular.z = ang_vel
	if msg.ranges[0] < 1: # if object to the right is at a distance smaller than 1
		move.linear.x = 0.0
		move.angular.z = ang_vel
	if msg.ranges[719] < 1: # if object to the left is at a distance smaller than 1
		move.linear.x = 0.0
		move.angular.z = -ang_vel
	pub.publish(move)


pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # publisher
sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback) # subscriber

rospy.spin()