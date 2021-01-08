#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty as Empty
from std_srvs.srv import Trigger, TriggerResponse
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
import time

class Drone_Class:

    def __init__(self):
        
        # init service
        my_serv = rospy.Service("my_service", Trigger, self.callback)

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

    ###

    def callback(self, request):
        self.response = TriggerResponse()
        self.response.message = ("Error while moving drone")
        self.response.success = False

        self.pose_sub = rospy.Subscriber("/drone/gt_pose", Pose, self.callback_pose)
        self.pose_msg = Pose()
        
        # takeoff
        self.takeoff_func()

        # get init pose
        self.init_pose = self.get_pose()
        rospy.sleep(1)
        print(self.init_pose)

        # move
        self.move_forward_func()
        rospy.sleep(5)
        self.stop_func()

        # get final pose
        self.final_pose = self.get_pose() 
        rospy.sleep(1)
        print(self.final_pose)

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
        self.move.linear.x = 1
        self.move.linear.y = 0
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