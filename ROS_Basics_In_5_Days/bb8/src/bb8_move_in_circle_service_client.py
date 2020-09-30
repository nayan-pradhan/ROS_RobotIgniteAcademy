#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

rospy.init_node('bb8_client_node')
rospy.wait_for_service('/move_bb8_in_circle')
move_bb8_in_circle_client = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

result = move_bb8_in_circle_client(EmptyResponse())
print result