#! /usr/bin/env python

import actionlib
import rospy
import time

#from actionlib.msg import TestFeedback, TestResult, TestAction
from action_quiz.msg import CustomActionFeedback, 
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class MoveDroneSquare(object):

    # create message obj that are used to publish feedback and result
    _feedback = TestFeedback()
    _result = TestResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer("action_custom_msg", TestAction, self.goal_callback, False)
        self._as.start()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)

    def publish_once_in_cmd_vel(self, cmd):
        while not self.ctrl_c:
            connections = self._pub_cmd_vel.get_num_connections()
            if connections > 0:
                self._pub_cmd_vel.publish(cmd)
                rospy.loginfo("Publish in cmd_vel")
                break
            else:
                self.rate.sleep()
    
    def stop_drone(self):
        rospy.loginfo("Stopping drone!")
        self._move_drone.linear.x = 0
        self._move_drone.angular.z = 0
        self.publish_once_in_cmd_vel(self._move_drone)

    def turn_drone(self):
        rospy.loginfo("Turning!")
        self._move_drone.linear.x = 0
        self._move_drone.angular.z = 1
        self.publish_once_in_cmd_vel(self._move_drone)

    def forward_drone(self):
        rospy.loginfo("Moving forward!")
        self._move_drone.linear.x = 1
        self._move_drone.angular.z = 0
        self.publish_once_in_cmd_vel(self._move_drone)
    
    def goal_callback(self, goal):
        r = rospy.Rate(1)
        success = True 

        self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self._move_drone = Twist()

        if (self.goal == "TAKEOFF"):
            self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size = 1)
            self._takeoff_msg = Empty()
        if (self.goal == "LAND"):
            self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size = 1)
            self._land_msg = Empty()

        # make the drone takeofff
        for i in range(1,4):
            self._pub_takeoff.publish(self._takeoff_msg)
            rospy.loginfo("Taking offf")
            time.sleep(1)
        
        sideSeconds = goal.goal
        turnSeconds = 2

        for i in xrange(0,4):
            # check for preempt (cancelation) request
            if self._as.is_preempt_requested():
                rospy.login_info("Goal has been cancelled!")
                self._as.set_preempted()
                success = False
                break

            # to move
            self.forward_drone()
            time.sleep(sideSeconds)
            self.turn_drone()
            time.sleep(sideSeconds)

            self._feedback.feedback = i
            self._as.publish_feedback(self._feedback)
            r.sleep

        if success:
            self._result.result = (sideSeconds*4) + (turnSeconds*4)
            rospy.loginfo("The total seconds it took the drone to perform the square was %i" % self._result.result)
            self._as.set_succeeded(self._result)

            self.stop_drone()
            for i in range(1,4):
                self._pub_land.publish(self._land_msg)
                rospy.loginfo("Landing!!!")
                time.sleep(1)
                i += 1

if __name__ == "__main__":
    rospy.init_node('action_custom_msg_node')
    MoveDroneSquare()
    rospy.spin()