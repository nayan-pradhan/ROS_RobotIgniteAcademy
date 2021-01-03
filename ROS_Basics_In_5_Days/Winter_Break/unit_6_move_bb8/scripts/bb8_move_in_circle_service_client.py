#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest
import sys

rospy.init_node("node_unit_6_bb8_client")
rospy.wait_for_service("/move_bb8_in_circle")
move_bb8_in_circle_service = rospy.ServiceProxy("/move_bb8_in_circle", Empty)
move_bb8_in_circle_service_object = EmptyRequest()
result = move_bb8_in_circle_service(move_bb8_in_circle_service_object)