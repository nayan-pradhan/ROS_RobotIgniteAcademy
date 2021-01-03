#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

def callback(request):
    print ("Callback has been called")
    move.linear.x = 0.5
    move.angular.z = 0.5
    pub.publish(move)
    return EmptyResponse()

rospy.init_node("node_unit_6_bb8")
my_service = rospy.Service("/move_bb8_in_circle", Empty, callback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
move = Twist()
rospy.spin()