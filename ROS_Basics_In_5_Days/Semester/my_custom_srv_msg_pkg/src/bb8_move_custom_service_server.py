#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from time import sleep

def call_back(request):
    my_response = MyCustomServiceMessageResponse()
    countdown = my_response.duration
    if (countdown < 0):
        my_response.success = False
        return my_response
    while (countdown > 0):
        move.linear.x = 0.2
        move.angular.z = 0.2
        pub.publish(move)
        countdown = countdown - 1 
        sleep(1)
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    my_response.success = True
    return my_response

rospy.init_node('Custom_Service_Server_Node')
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, call_back)
move = Twist()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
rospy.spin()