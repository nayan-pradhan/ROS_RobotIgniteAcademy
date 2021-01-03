#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest
import sys

rospy.init_node("node_call_bb8_move_custom_service_server")
rospy.wait_for_service("/move_bb8_in_circle_custom")
move_service = rospy.ServiceProxy("/move_bb8_in_circle_custom", MyCustomServiceMessage)
move_object = MyCustomServiceMessageRequest()
move_object.duration = 10
result = move_service(move_object)
print(result)