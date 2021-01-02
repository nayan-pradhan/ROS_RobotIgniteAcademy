#! /usr/bin/env python 

# not working

import rospy
from odometry_pkg.msg import Age

rospy.init_node("node_odom_publisher")
pub = rospy.Publisher("/odom", Age, queue_size=1)
change_age = Age()

while not rospy.is_shutdown():
    change_age.years = 2.8
    chage_age.months = 3.1
    change_age.days = 9.23

    pub.publish(change_age)