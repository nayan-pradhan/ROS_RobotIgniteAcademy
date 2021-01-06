#! /usr/bin/env python

import rospy
import actionlib
from actionlib.msg import TestFeedback, TestResult, TestAction
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time

class DroneClass(object):
    # create messages taht are used to publish feedback and result
    _feedback = TestFeedback()
    _result = TestResult()

    def __init__(self):
        # create action server
        self._as = actionlib.SimpleActionServer("drone_square_as", TestAction, self.goal_callback, False)
        self._as.start() 
    
    def takeoff_func(self):
        rospy.loginfo("Taking off ...")
        self.pub_takeoff.publish(self.takeoff)
        rospy.sleep(3)
        rospy.loginfo("Took off!")
    
    def stop_func(self):
        rospy.loginfo("Stopping ...")
        # linear x controls forward (+1) and backword (-1)
        # linear y controls left (+1) and right (-1)
        # linear z controls up (+1) and down (-1)
        self.move.linear.x = 0
        self.move.linear.y = 0
        self.move.linear.z = 0
        # angular z controls CCV(+1) and CV (-1)
        self.move.angular.z = 0
        self.pub_move.publish(self.move)
        rospy.sleep(2)
        rospy.loginfo("Stopped!")

    def forward_func(self, time_move):
        rospy.loginfo("Moving forward ...")
        # linear x controls forward (+1) and backword (-1)
        # linear y controls left (+1) and right (-1)
        # linear z controls up (+1) and down (-1)
        self.move.linear.x = 0.5
        self.move.linear.y = 0
        self.move.linear.z = 0
        # angular z controls CCV(+1) and CV (-1)
        self.move.angular.z = 0
        self.pub_move.publish(self.move)
        rospy.sleep(self.time_move)
        rospy.loginfo("Moved forward!")
    
    def turn_right_func(self):
        rospy.loginfo("Turning right ...")
        # linear x controls forward (+1) and backword (-1)
        # linear y controls left (+1) and right (-1)
        # linear z controls up (+1) and down (-1)
        self.move.linear.x = 0
        self.move.linear.y = 0
        self.move.linear.z = 0
        # angular z controls CCV(+1) and CV (-1)
        self.move.angular.z = -0.5
        self.pub_move.publish(self.move)
        rospy.sleep(3)
        rospy.loginfo("Turned right!")
    
    def land_func(self):
        rospy.loginfo("Landing ...")
        self.pub_land.publish(self.land)
        rospy.sleep(3)
        rospy.loginfo("Landed!")

    def goal_callback(self, goal):

        success = True 

        print("IN CALLBACK")

        # create publishers
        self.pub_move = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        while self.pub_move.get_num_connections() < 1:
            rospy.sleep(1)
        self.move = Twist()

        self.pub_takeoff = rospy.Publisher("/drone/takeoff", Empty, queue_size=1)
        while self.pub_takeoff.get_num_connections() < 1:
            rospy.sleep(1)
        self.takeoff = Empty()

        self.pub_land = rospy.Publisher("/drone/land", Empty, queue_size=1)
        while self.pub_land.get_num_connections() < 1:
            rospy.sleep(1)
        self.land = Empty()
        
        self.time_move = goal.goal # because callback has goal in param

        # takeoff
        self.takeoff_func()
        start_time = time.time() # start time
        for i in xrange(0, 4):
            if self._as.is_preempt_requested():
                rospy.loginfo("Goal canceled/preemped")
                self._as.set_preempted()
                success = False
                break
            self.forward_func(self.time_move)
            self.stop_func()
            self.turn_right_func()
            self.stop_func()

            # feedback
            self._feedback.feedback = i
            self._as.publish_feedback(self._feedback)
            rospy.sleep(1)
        stop_time = time.time() # stop time
        # land
        self.land_func()

        if success:
            self._result.result = stop_time - start_time
            self._as.set_succeeded(self._result)
            rospy.loginfo("Success")

if __name__ == "__main__":
    rospy.init_node("node_drone_square_action_server")
    DroneClass()
    rospy.spin()