#! /usr/bin/env python

import rospy
import actionlib
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import LaserScan 
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Twist
from time import sleep


class EscapeRoomService(object):

    def __init__(self):

        # depth sensor subscriber
        self.my_pc_sub = rospy.Subscriber("/camera/depth/points", PointCloud2, self.callback_pc)
        self.pc_msg = PointCloud2()

        # laser subscriber
        self.my_laser_sub = rospy.Subscriber("/camera/scan", LaserScan, self.callback_laser)
        self.laser_msg = LaserScan()

        # publisher
        self.pub = rospy.Publisher("/husky_velocity_controller/cmd_vel", Twist, queue_size = 1)
        while self.pub.get_num_connections() < 1:
            sleep(1)
        self.move = Twist()

        # init service
        self.my_service = rospy.Service("/crash_direction_service", Trigger, self.callback_serv)

    ###

    def callback_serv(self, request):
        self.response = TriggerResponse()
        self.response.success = False 
        self.response.message = "Not Successfull"

        self.front = self.get_laser().ranges[89]
        self.left = self.get_laser().ranges[180]
        self.right = self.get_laser().ranges[0]

        # print(self.left, self.front, self.right)

        if self.front>=self.left and self.front>=self.right:
            self.response.success = True
            self.response.message = "front"
        
        if self.left>=self.front and self.left>=self.right:
            self.response.success = True
            self.response.message = "left"

        if self.right>=self.front and self.right>=self.left:
            self.response.success = True
            self.response.message = "right"

        # if self.front > 2:
        #     self.response.success = True
        #     self.response.message = "front"
        
        # elif self.left > 2:
        #     elf.response.success = True
        #     self.response.message = "left"

        # elif self.right > 2:
        #     elf.response.success = True
        #     self.response.message = "right"

        # print(self.front, self.left, self.right)

        # self.turn_right()
        # self.turn_left()
        # self.turn_left()

        # self.front = self.get_depth()
        # # print(self.front)
        # for j in xrange(10):
        #     self.front = self.get_depth()
        #     if (self.front == False):
        #         self.response.success = True 
        #         self.response.message = "front"
        #         break
        #     else:
        #         self.front = self.get_depth()
        #         self.turn_right()
        #         self.stop_moving()
        #         if (self.front == False):
        #             self.response.success = True
        #             self.response.message = "right"
        #             break
        #         else:
        #             self.front = self.get_depth()
        #             self.turn_left()
        #             self.stop_moving()
        #             self.turn_left()
        #             self.stop_moving()
        #             if (self.front == False):
        #                 self.response.success = True
        #                 self.response.message = "left"
        #                 break

        return self.response


    ###

    def callback_pc(self, msg):
        self.pc_msg = msg.is_dense  
    
    def get_depth(self):
        return self.pc_msg

    def callback_laser(self, msg):
        self.laser_msg = msg
    
    def get_laser(self):
        return self.laser_msg

    ###

    def turn_right(self):
        for i in xrange(0, 9):
            rospy.loginfo("Turning Right")
            self.move.linear.x = 0.1
            self.move.angular.z = -0.9
            self.pub.publish(self.move)
            sleep(1)
        rospy.loginfo("Turned Right")
        # self.stop_moving()

    def turn_left(self):
        for i in xrange(0, 9):
            rospy.loginfo("Turning Left")
            self.move.linear.x = -0.1
            self.move.angular.z = 0.9
            self.pub.publish(self.move)
            sleep(1)
        rospy.loginfo("Turned Left")
        # self.stop_moving()
        
    def stop_moving(self):
        rospy.loginfo("Stoping")
        self.move.linear.x = 0
        self.move.angular.z = 0
        self.pub.publish(self.move)
        sleep(0.5)


if __name__ == "__main__":
    rospy.init_node("node_exam_service_server")
    EscapeRoomService()
    rospy.spin()