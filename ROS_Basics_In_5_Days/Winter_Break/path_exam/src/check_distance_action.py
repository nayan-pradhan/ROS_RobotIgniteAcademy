#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty as Empty
from std_srvs.srv import Trigger, TriggerResponse
from geometry_msgs.msg import Twist, Pose
import actionlib
from path_exam.msg import RecordOdomAction, RecordOdomFeedback, RecordOdomResult
import time

class Drone_Class:

    _feedback = RecordOdomFeedback()
    _result = RecordOdomResult()

    def __init__(self):

        # pose subscriber
        self.pose_sub = rospy.Subscriber("/drone/gt_pose", Pose, self.callback_pose)
        self.pose_msg = Pose()

         # init publishers
        self.pub_takeoff = rospy.Publisher("/drone/takeoff", Empty, queue_size=1)
        while self.pub_takeoff.get_num_connections() < 1:
            rospy.sleep(1)

        self.pub_move = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        while self.pub_move.get_num_connections() < 1:
            rospy.sleep(1)
        self.move = Twist()

        self.pub_land = rospy.Publisher("/drone/land", Empty, queue_size=1)
        while self.pub_land.get_num_connections() < 1:
            rospy.sleep(1)
        
        # init service
        self.my_serv = rospy.Service("my_service", Trigger, self.callback)

        # init action server
        self._as = actionlib.SimpleActionServer("rec_pose_as", RecordOdomAction, self.as_callback, False)
        self._as.start() 

    ###
        
    def as_callback(self, goal):
        success = True
        if self._as.is_preempt_requested():
            rospy.loginfo("Goal canceled/preemped")
            self._as.set_preempted()
            success = False
            rospy.loginfo("ACTION FAILED")
            quit()
        self._result.result_list = []
        for i in xrange(0, 20):
            self.x_coordinate = self.get_pose()
            self._result.result_list.append(self.x_coordinate)
            rospy.sleep(1)
        # print("Arr: ",  self._result.result_list)
        self._feedback = Empty()
        
        if success:
            self._as.set_succeeded(self._result)
            rospy.loginfo("Success")

    ###

    def callback(self, request):
        self.response = TriggerResponse()
        self.response.message = ("Error while moving drone")
        self.response.success = False
        
        # takeoff
        self.takeoff_func()

        # get init pose
        self.init_pose = self.get_pose()
        rospy.sleep(1)
        # print(self.init_pose)

        # move
        self.move_forward_func()
        rospy.sleep(5)
        self.stop_func()

        # get final pose
        self.final_pose = self.get_pose() 
        rospy.sleep(1)
        # print(self.final_pose)

        # land
        self.land_func()
        
        diff = self.final_pose - self.init_pose 

        if diff != 0:
            self.response.message = ("The drone has moved %f meteres" %diff)
            self.response.success = True
        return self.response

    ### 

    def callback_pose(self, msg):
        self.pose_msg = msg

    def get_pose(self):
        return self.pose_msg.position.x

    ###

    def takeoff_func(self):
        rospy.loginfo("Taking off ...")
        self.pub_takeoff.publish(Empty())
        rospy.sleep(2)
        rospy.loginfo("Took off!")

    def land_func(self):
        rospy.loginfo("Landing ...")
        self.pub_land.publish(Empty())
        rospy.sleep(2)
        rospy.loginfo("Landed!")

    def move_forward_func(self):
        rospy.loginfo("Moving forward ...")
        # linear x controls forward (+1) and backword (-1)
        # linear y controls left (+1) and right (-1)
        # linear z controls up (+1) and down (-1)
        self.move.linear.x = 0.5
        self.move.linear.z = 0
        # angular z controls CCV(+1) and CV (-1)
        self.move.angular.z = 0
        rospy.loginfo("Moved forward!")
        self.pub_move.publish(self.move)

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
        rospy.sleep(2)
        rospy.loginfo("Stopped!")
        self.pub_move.publish(self.move)

    ###

if __name__ == "__main__":
    rospy.init_node("node_distance_motion_service")
    Drone_Class()
    rospy.spin()