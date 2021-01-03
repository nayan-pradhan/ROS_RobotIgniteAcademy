#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

def callback(request):
    print "Callback has been called"
    return EmptyResponse()
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node("service_server")
my_service = rospy.Service("/my_service", Empty, callback)
rospy.spin()