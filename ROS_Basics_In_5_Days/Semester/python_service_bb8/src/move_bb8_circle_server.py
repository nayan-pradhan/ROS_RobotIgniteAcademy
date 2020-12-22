#! /usr/bin/env python

import rospy
from python_service_bb8.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def call_back(request):
    rospy.loginfo("Service move_bb8_in_circle called")
    movebb8_custom_obj = MoveBB8_custom()
    movebb8_custom_obj.move_bb8()
    rospy.loginfo("Finished service /move_bb8_in_circle_custom")
    return MyCustomServiceMessageResponse()

rospy.init_node('bb9_circle_server_node')
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, call_back)
rospy.loginfo("Service /move_bb8_in_circle_custom ready")
rospy.spin()
