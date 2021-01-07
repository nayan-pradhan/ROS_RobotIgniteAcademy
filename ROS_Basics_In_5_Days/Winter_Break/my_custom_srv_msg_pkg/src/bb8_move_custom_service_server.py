#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

def callback(request):
    print "Move bb8 in circle request received in server"

    # move for duration
    move.linear.x = 0.5
    move.angular.z = 0.5
    pub.publish(move)
    sleep_time = request.duration
    rospy.sleep(sleep_time)

    # after duration stop 
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)

    response = MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node("node_bb8_move_custom_service_server")
my_service = rospy.Service("/move_bb8_in_circle_custom", MyCustomServiceMessage, callback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
move = Twist()
rospy.spin()