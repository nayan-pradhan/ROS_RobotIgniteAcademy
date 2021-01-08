#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty
rospy.init_node("node_drone_takeoff")

pub_takeoff = rospy.Publisher("/drone/takeoff", Empty, queue_size=1)
while pub_takeoff.get_num_connections() < 1:
    rospy.sleep(1)

pub_takeoff.publish(Empty())
