#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Image, PointCloud2, PointField
from time import sleep


def callback_pc(msg):
    print("Is Dense: ")
    print(msg.is_dense)

def callback_rgb(msg):
    print("Is RGB:")
    print msg.is_bigendian

rospy.init_node("Node_MyCamSub")
sub_rgb = rospy.Subscriber("/camera/rgb/image_raw", Image, callback_rgb)

sub_pc = rospy.Subscriber("/camera/depth/points", PointCloud2, callback_pc)
rospy.spin()

# def callback_dep(msg):
#     print ("Image Depth msg: ")
#     print msg

# def callback_rgb(msg):
#     print ("RGB Image msg: ")
#     print msg


# sub_dep = rospy.Subscriber("/camera/depth/image_raw", Image, callback_dep)

