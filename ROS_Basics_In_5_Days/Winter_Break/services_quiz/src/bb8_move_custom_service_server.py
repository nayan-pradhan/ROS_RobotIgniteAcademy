#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def callback(request):
    dist = request.side #* 2 # times 2 just so that the square is not too small
    rep = request.repetitions
    response = BB8CustomServiceMessageResponse()

    if (dist <= 0 or rep <= 0):
        response.success = False
        return response

    i = 0 # how many times we are repeting square
    while i < rep:
        # print("i=",i)
        j = 0 # four sides of square
        while j < 4:
            # print("j=",j)
            move_straight()
            rospy.sleep(dist)
            # rospy.sleep(1) 

            turn_right()   
            rospy.sleep(3.365)
            # stop()
            # rospy.sleep(1)     
            j = j + 1
        i = i + 1
        print("number of Repetations complete:", i)
    stop()
    print("Service Complete")
    response.success = True
    return response

def move_straight():
    move.linear.x = 0.5
    move.angular.z = 0.0
    pub.publish(move)

def turn_right():
    move.linear.x = 0.0
    move.angular.z = 0.5
    rospy.sleep(1)
    pub.publish(move)

def stop():
    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)

rospy.init_node("node_bb8_move_custom_service_server")
my_service = rospy.Service("/move_bb8_in_square_custom", BB8CustomServiceMessage, callback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
move = Twist()
rospy.spin()