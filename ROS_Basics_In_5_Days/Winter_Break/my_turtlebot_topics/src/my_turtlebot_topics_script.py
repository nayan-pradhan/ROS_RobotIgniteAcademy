#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan 

class OdomSub(object):
    def __init__(self):
        self.my_Odom_Sub = rospy.Subscriber("/odom", Odometry, callback_odom)
    
class LaserSub(object):
    def __init__(self):
        self.my_laser_sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback_laser)

def callback_odom(msg):
    for i in xrange(1, 3):
        rospy.loginfo("Pose:")
        print msg.pose
        rospy.sleep(1)

def callback_laser(msg):
        for i in xrange(1, 3):
            rospy.loginfo("Laser:")
            print msg.ranges[360]

if __name__ == "__main__":
    rospy.init_node("node_my_turtlebot_topics_script")
    OdomSub()
    rospy.sleep(1)
    LaserSub()
    rospy.spin()
