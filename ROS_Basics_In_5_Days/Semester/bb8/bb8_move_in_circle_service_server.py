#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

def call_back(request):
    print "Callback has been called!"
    move.linear.x = 0.5
    move.angular.z = 0.5
    pub.publish(move)
    return EmptyResponse()

move = Twist()
rospy.init_node('bb8_service_node')
my_service = rospy.Service('/move_bb8_in_circle', Empty, call_back)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
move = Twist()

rospy.spin()