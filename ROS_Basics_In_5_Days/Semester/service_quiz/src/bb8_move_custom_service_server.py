#! /usr/bin/env python

import rospy
from service_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
from time import sleep

def call_back(request):
    dist = request.side * 2 # times 2 just so that the square is not too small
    rep = request.repetitions
    response = BB8CustomServiceMessageResponse()

    if (dist <= 0 or rep <= 0):
        response.success = False
        return response

    i = 0 # how many times we are repeting square
    while i < rep:
        j = 0 # four sides of square
        while j < 4:
            move_straight()
            rospy.sleep(dist)
            turn_right()   
            rospy.sleep(1)     
            j += 1
        i += 1
    response.success = True
    return response

def move_straight():
    move.linear.x = 0.5
    move.angular.z = 0.0
    pub.publish(move)

def turn_right():
    move.linear.x = 0.0
    move.angular.z = 0.5
    pub.publish(move)

# def call_back(request):
#     my_response = BB8CustomServiceMessageResponse()
#     how_many_repeat = request.repetitions

#     if (request.side <= 0 or request.repetitions <= 0):
#         my_response.success = False
#         return my_response

#     while (how_many_repeat != 0):
#         side_number = 0
#         size_of_square = 2 * request.side
#         while (side_number < 4):
#             move.linear.x = 0.5
#             sleep(how_many_repeat)
#             move.angular.z = 0.5
#             pub.publish(move)
#             sleep(1)
#             side_number = side_number + 1
#         how_many_repeat = how_many_repeat - 1

#     move.linear.x = 0
#     move.angular.z = 0
#     pub.publish(move)
#     my_response.success = True

#     return my_response

rospy.init_node('/custom_service_server_node')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, call_back)
move = Twist()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin()