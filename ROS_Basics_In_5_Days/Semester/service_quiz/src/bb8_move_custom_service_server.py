#! /usr/bin/env python

import rospy
from service_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
from time import sleep

def call_back(request):
    my_response = BB8CustomServiceMessageResponse()
    how_many_repeat = my_response.repetitions

    if (side <= 0 or repetitions <= 0):
        my_response.success = False
        return my_response

    while (how_many_repeat != 0):
        side_number = 0
        size_of_square = 2 * my_response.side
        while (side_number < 4):
            move.linear.x = 0.5
            sleep(how_many_repeat)
            move.angular.z = 0.5
            pub.publish(move)
            sleep(1)
            side_number = side_number + 1
        how_many_repeat = how_many_repeat - 1

    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    my_response.success = True

    return my_response

rospy.init_node('/custom_service_server_node')
my_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage, call_back)
move = Twist()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin()