#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node("node_call_bb8_move_custom_service_server")
rospy.wait_for_service("/move_bb8_in_square_custom")
my_service = rospy.ServiceProxy("/move_bb8_in_circle_custom", BB8CustomServiceMessage)

my_service_object_small = BB8CustomServiceMessageRequest()
my_service_object_small.side = 5
my_service_object_small.repetitions = 2
result_small = my_service(my_service_object_small)
print(result_small)

my_service_object_large = BB8CustomServiceMessageRequest()
my_service_object_large.side = 10
my_service_object_large.repetitions = 1
result_large = my_service(my_service_object_large)
print(result_large)