#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

def callback(request):
    print "Callback has been called"
    return EmptyResponse()

rospy.init_node("service_server")
my_service = rospy.Service("/my_service", Empty, callback)
rospy.spin()