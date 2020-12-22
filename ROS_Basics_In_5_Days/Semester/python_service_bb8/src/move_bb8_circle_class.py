#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from my_python_class.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from timer import sleep

class MoveBB8_custom():

    def __init__(self):
        self.bb8_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        while not self.ctrl_c:
            connections = self.bb8_publisher.get_num_connections()
            if connections > 0:
                self.bb8_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep

    def shutdownhook(self):    
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()
        self.ctrl_c = True

    def move_bb8(self, linear_speed=0.2, angular_speed=0.2):
        my_response = MyCustomServiceMessage()
        countdown = my_response.duration
        if (countdown <= 0):
            my_response = False
            return my_response
        while (countdown > 0):
            self.cmd.linear.x = linear_speed
            self.cmd.angular.z = angular_speed
            rospy.loginfo("Moving BB8")
            self.publish_once_in_cmd_vel()
            countdown = countdown - 1
            sleep(1)
        # after process complete
        rospy.loginfo("Timer Complete")
        my_response = True
        return my_response

if __name__ == '__main__':
    rospy.init_node('move_bb8_node', anonymous=True)
    move_bb8_object = move_bb8()
    try:
        move_bb8_object.move_bb8() 
    except rospy.ROSInterruptException:
        pass