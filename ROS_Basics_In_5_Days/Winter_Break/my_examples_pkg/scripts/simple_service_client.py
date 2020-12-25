#! /usr/bin/env python

import rospy
from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest # Import the service message used by the service /trajectory_by_name
import sys

rospy.init_node("service_client") # initialize ros node
rospy.wait_for_service("/trajectory_by_name") # wait for service client to be running
traj_by_name_service = rospy.ServiceProxy("/trajectory_by_name", TrajByName) # create connection with service
traj_by_name_object = TrajByNameRequest() # create object of type
traj_by_name_object.traj_name = "release_food" # fill variable traj_name of object with desired value
result = traj_by_name_service(traj_by_name_object) # send through connection the name of trajcetory to be executed by robot

print result