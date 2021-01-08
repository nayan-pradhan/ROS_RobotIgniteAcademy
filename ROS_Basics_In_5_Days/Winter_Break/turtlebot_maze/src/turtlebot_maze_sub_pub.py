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
    rospy.loginfo("Pose:")
    print msg.pose
    rospy.sleep(0.5)

def callback_laser(msg):
        rospy.loginfo("Laser:")
        print msg.ranges[360]
        rospy.sleep(1)

if __name__ == "__main__":
    rospy.init_node("node_turtlebot_maze_sub_pub")
    OdomSub()
    LaserSub()
    rospy.spin()
