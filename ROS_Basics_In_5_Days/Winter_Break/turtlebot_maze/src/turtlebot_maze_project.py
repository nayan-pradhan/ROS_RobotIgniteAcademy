#! /usr/bin/env python

import rospy
import actionlib
from turtlebot_maze.msg import MyTurtlebotMazeActionFeedback, MyTurtlebotMazeActionAction, MyTurtlebotMazeActionResult
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan 
from time import sleep
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import Empty

class Maze(object):

    _feedback = MyTurtlebotMazeActionFeedback()
    _result = MyTurtlebotMazeActionResult()

    def __init__(self):

        # odom subscriber
        self.my_Odom_Sub = rospy.Subscriber("/odom", Odometry, self.callback_odom)
        self.odom_msg = Odometry()

        # laser subscriber
        self.my_laser_sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, self.callback_laser)
        self.laser_msg = LaserScan()

        # init service
        self.my_service = rospy.Service("/turtlebot_maze_service_server", Trigger, self.callback_serv)
        
        # init action
        self._as = actionlib.SimpleActionServer("/turtlebot_maze_action_server", MyTurtlebotMazeActionAction, self.as_goal_callback, False)
        self._as.start()

        # publisher
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
        while self.pub.get_num_connections() < 1:
            sleep(1)
        self.move = Twist()
    
    ###

    def as_goal_callback(self, goal):
        self.stop_prog = False
        self.success = False
        self._feedback = Empty()
        self.total_time = 90
        self.init_pos = self.get_odom()
        # print ("Initial x = ", self.init_pos.pose.pose.position.x)
        self._result.result_odom_array = []
        # checks time
        for self.current_time in xrange(1, self.total_time+1):
            self.current_pos = self.get_odom()
            self._result.result_odom_array.append(self.current_pos)
            # checks end of maze
            # print(self.init_pos.pose.pose.position.y - self.current_pos.pose.pose.position.y)
            if (self.init_pos.pose.pose.position.y - self.current_pos.pose.pose.position.y) > 9:
                rospy.loginfo("Turtlebot has exited maze")
                self.success = True
                self.stop_prog = True
                break
            if (self.current_time == self.total_time):
                self.stop_prog = True
                rospy.loginfo("Failed, total time exceeded")
                break
            sleep(1)
        if self.success:
            # print("RESULT =>", self._result.result_odom_array)
            self._as.set_succeeded(self._result)
            rospy.loginfo("Success from action server")

    ###

    def callback_serv(self, request):
        self.response = TriggerResponse()
        self.response.success = False 
        self.response.message = "Not successfull"

        # drive part
        while not self.stop_prog:
            front = self.get_laser().ranges[360]
            left = self.get_laser().ranges[719]
            right = self.get_laser().ranges[0]
            # print(front, left, right)
            
            if (front >= 2):
                self.move_forward_fast()
                sleep(0.5)

            elif (front < 2) and (front > 0.8):
                self.move_forward_slow()
                sleep(0.2)
            
            elif (front > 0.2 and front < 0.8) and (right > left):
                self.stop_moving() 
                self.turn_right()
            
            elif (front > 0.2 and front < 0.8) and (left > right):
                self.stop_moving()
                self.turn_left()
            
            elif (front < 0.2):
                self.back_up()
                sleep(0.2)

        if self.stop_prog:
            self.stop_moving()
            sleep(0.5)
            rospy.loginfo("Service completed")
            if (self.success):
                self.response.message = "Successfull movement"
                self.response.success = True
        
        return self.response
    ###
    
    def move_forward_fast(self):
        self.move.linear.x = 1.0
        self.move.angular.z = 0.0
        self.pub.publish(self.move)

    def move_forward_slow(self):
        self.move.linear.x = 0.25
        self.move.angular.z = 0.0
        self.pub.publish(self.move)

    def stop_moving(self):
        self.move.linear.x = 0.0
        self.move.angular.z = 0.0
        self.pub.publish(self.move)

    def back_up(self):
        self.move.linear.x = -0.3
        self.move.angular.z = 0.0
        self.pub.publish(self.move)

    def turn_right(self):
        self.front = self.get_laser().ranges[360]
        while (self.front < 3):
            self.move.linear.x = 0
            self.move.angular.z = -0.4
            self.pub.publish(self.move)
            self.front = self.get_laser().ranges[360]
            sleep(0.3)
        self.stop_moving()

    def turn_left(self):
        self.front = self.get_laser().ranges[360]
        while (self.front < 3):
            self.move.linear.x = 0
            self.move.angular.z = 0.4
            self.pub.publish(self.move)
            self.front = self.get_laser().ranges[360]
            sleep(0.3)
        self.stop_moving()

    ###

    def callback_odom(self, msg):
        self.odom_msg = msg  
    
    def get_odom(self):
        return self.odom_msg
    
    ###

    def callback_laser(self, msg):
        self.laser_msg = msg
    
    def get_laser(self):
        return self.laser_msg
    
    ###

if __name__ == "__main__":
    rospy.init_node("node_turtlebot_maze_project")
    Maze()
    rospy.spin()