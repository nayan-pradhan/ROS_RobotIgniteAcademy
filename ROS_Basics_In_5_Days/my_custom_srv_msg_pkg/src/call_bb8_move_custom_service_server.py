#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('bb8_move_custom_service_client_server_node')
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_custom_service_client_server = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

result = move_bb8_custom_service_client_server(MyCustomServiceMessageRequest)
print result

# create a subscriber to get my message