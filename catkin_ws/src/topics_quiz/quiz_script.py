#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 

rospy.init_node('topics_quiz_node') # initialize node

# rate = rospy.Rate(10) 
# while not rospy.is_shutdown():
#     rate.sleep()

moveRobot = Twist() # Creating object  
def call_back(msg):
    if msg.ranges[360] > 1: # 360 is front
        moveRobot.linear.x = 0.4
        moveRobot.angular.z = 0 # move forward
    if msg.ranges[360] < 1: # 360 is front
        moveRobot.linear.x = 0.0
        moveRobot.angular.z = 0.2 # turn left
    if msg.ranges[0] < 1: # 0 is right
        moveRobot.linear.x = 0.0
        moveRobot.angular.z = 0.2 # turn left
    if msg.ranges[719] < 1: # 719 is left
        moveRobot.linear.x = 0.0
        moveRobot.angular.z = -0.2 # turn right
    pub.publish(moveRobot)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # for publisher
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, call_back) # for subscriber

rospy.spin() 

# COMMENT TO SELF
# Here values go from 0 - 719 degrees as mentioned in HINT4