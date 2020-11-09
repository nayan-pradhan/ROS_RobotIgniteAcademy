#! /usr/bin/env python

import rospy
import time
import tf
from turtle_tf_3d.get_model_gazebo_pose import GazeboModel

def handle_turtle_pose(pose_msg, robot_name):
    br = tf.TransformBroadcaster()
    
    br.sendTransform((pose_msg.position.x,pose_msg.position.y,pose_msg.position.z),
                     (pose_msg.orientation.x,pose_msg.orientation.y,pose_msg.orientation.z,pose_msg.orientation.w),
                     rospy.Time.now(),
                     robot_name,
                     "/world")


def publisher_of_tf():
    # initialize publisher node
    rospy.init_node('publisher_of_tf_node', anonymous = True)
    # initializing list to use later
    robot_name_list = ["turtle1", "turtle2"]
    # gives position and orientation of Gazebo Model in simulation
    gazebo_model_object = GazeboModel(robot_name_list)

    # iterating through robots to get pose
    for robot in robot_name_list:
        pose_now = gazebo_model_object.get_model_pose(robot)
    
    # leave some time to be sure Gazebo Model logs have finished
    time.sleep(1)
    rospy.loginfo("Ready..Starting to Publish TF data")

    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        for robot in robot_name_list:
            pose_now = gazebo_model_object.get_model_pose(robot)
            # if fail
            if not pose_now:
                print "The " + str(robot) + " 's pose in unavailabe right now. Try again later! ..."
            # if success
            else:
                # pass it into my publisher
                handle_turtle_pose(pose_now, robot)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_of_tf()
    except rospy.ROSInterruptException:
        pass