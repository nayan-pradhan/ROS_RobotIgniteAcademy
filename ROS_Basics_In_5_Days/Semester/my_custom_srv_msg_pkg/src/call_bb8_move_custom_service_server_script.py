#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('bb8_move_custom_service_client_server_node')
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_custom_service_client_server = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

my_custom_service_msg_request_object = MyCustomServiceMessageRequest()
my_custom_service_msg_request_object.duration = 2

result = move_bb8_custom_service_client_server(my_custom_service_msg_request_object)
print result