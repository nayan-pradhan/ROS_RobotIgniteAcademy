#! /usr/bin/env python

import rospy
from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest
from iri_wam_reproduce_trajectory.srv import ExecTraj
import sys
#####
# This part is important to link the 'get_food.txt" part
import rospkg 
rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') \
        + "/config/get_food.txt"
#####

rospy.init_node('service_client')
rospy.wait_for_service('/execute_trajectory')
execute_trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Creating connection to server

result = execute_trajectory_service(traj)
print result
print ('----------')

# execute_trajectory_object = ExecTraj()
# execute_trajectory_object.execute_name = "get_food"
# result = execute_trajectory_service(execute_trajectory_object)
# print result