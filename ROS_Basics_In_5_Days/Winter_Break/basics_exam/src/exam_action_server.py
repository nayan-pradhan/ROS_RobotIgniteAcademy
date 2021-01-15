#! /usr/bin/env python

import rospy
import actionlib
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Twist
from time import sleep
from nav_msgs.msg import Odometry
from basics_exam.msg import record_odomAction, record_odomFeedback, record_odomResult

class EscapeRoom(object):

    _feedback = record_odomFeedback()
    _result = record_odomResult()

    def __init__(self):

        # # depth sensor subscriber
        # self.my_pc_sub = rospy.Subscriber("/camera/depth/points", PointCloud2, self.callback_pc)
        # self.pc_msg = PointCloud2()

        # # publisher
        # self.pub = rospy.Publisher("/husky_velocity_controller/cmd_vel", Twist, queue_size = 1)
        # while self.pub.get_num_connections() < 1:
        #     sleep(1)
        # self.move = Twist()

        # odom subscriber
        self.my_Odom_Sub = rospy.Subscriber("/odometry/filtered", Odometry, self.callback_odom)
        self.odom_msg = Odometry()

        # init action
        self._as = actionlib.SimpleActionServer("/rec_odom_as", record_odomAction, self.as_goal_callback, False)
        self._as.start()

        # # init service
        # self.my_service = rospy.Service("/crash_direction_service", Trigger, self.callback_serv)

    ###

    def as_goal_callback(self, goal):
        self._result.result_odom_array = []
        self.success_as = False
        # print (self.get_odom())
        for t in xrange(1, 61):
            self.current_pos = self.get_odom()
            self._result.result_odom_array.append(self.current_pos)
            sleep(1)
            if (t == 60):
                self.success_as = True
        print(self._result.result_odom_array)
        if (self.success_as):
            self._as.set_succeeded(self._result)
            rospy.loginfo("Success from action server")

    ###

    def callback_odom(self, msg):
        self.odom_msg = msg  
    
    def get_odom(self):
        return self.odom_msg

    # def callback_serv(self, request):

    #     self.response = TriggerResponse()
    #     self.response.success = False 
    #     self.response.message = "Not Successfull"

    #     # self.turn_right()
    #     # self.turn_left()
    #     # self.turn_left()

    #     self.front = self.get_depth()
    #     # print(self.front)
    #     for j in xrange(10):
    #         self.front = self.get_depth()
    #         if (self.front == False):
    #             self.response.success = True 
    #             self.response.message = "front"
    #             break
    #         else:
    #             self.front = self.get_depth()
    #             self.turn_right()
    #             self.stop_moving()
    #             if (self.front == False):
    #                 self.response.success = True
    #                 self.response.message = "right"
    #                 break
    #             else:
    #                 self.front = self.get_depth()
    #                 self.turn_left()
    #                 self.stop_moving()
    #                 self.turn_left()
    #                 self.stop_moving()
    #                 if (self.front == False):
    #                     self.response.success = True
    #                     self.response.message = "left"
    #                     break

    #     return self.response


    # ###

    # def callback_pc(self, msg):
    #     self.pc_msg = msg.is_dense  
    
    # def get_depth(self):
    #     return self.pc_msg

    # ###

    # def turn_right(self):
    #     for i in xrange(0, 9):
    #         rospy.loginfo("Turning Right")
    #         self.move.linear.x = 0.1
    #         self.move.angular.z = -0.9
    #         self.pub.publish(self.move)
    #         sleep(1)
    #     rospy.loginfo("Turned Right")
    #     # self.stop_moving()

    # def turn_left(self):
    #     for i in xrange(0, 9):
    #         rospy.loginfo("Turning Left")
    #         self.move.linear.x = -0.1
    #         self.move.angular.z = 0.9
    #         self.pub.publish(self.move)
    #         sleep(1)
    #     rospy.loginfo("Turned Left")
    #     # self.stop_moving()
        
    # def stop_moving(self):
    #     rospy.loginfo("Stoping")
    #     self.move.linear.x = 0
    #     self.move.angular.z = 0
    #     self.pub.publish(self.move)
    #     sleep(0.5)


if __name__ == "__main__":
    rospy.init_node("node_exam_action_server")
    EscapeRoom()
    rospy.spin()