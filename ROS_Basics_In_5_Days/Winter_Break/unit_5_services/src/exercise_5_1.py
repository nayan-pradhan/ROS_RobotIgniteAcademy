#! /usr/bin/env python

import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys
import rospkg
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

rospy.init_node("ex5_service_node")
rospy.wait_for_service("/execute_trajectory")
execute_trajectory_service = rospy.ServiceProxy("/execute_trajectory", ExecTraj)
execute_trajectory_object = ExecTrajRequest()
execute_trajectory_object.file = traj
result = execute_trajectory_service(execute_trajectory_object)
print result