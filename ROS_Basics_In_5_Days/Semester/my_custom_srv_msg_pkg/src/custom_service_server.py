#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def call_back(request):
    my_response = MyCustomServiceMessageResponse()
    if request.duration > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    return my_response

rospy.init_node('my_service_node')
my_service = rospy.Service('/my_service', MyCustomServiceMessage, call_back)

rospy.spin()
