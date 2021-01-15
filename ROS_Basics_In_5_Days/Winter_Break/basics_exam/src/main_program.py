#! /usr/bin/env python

import rospy
import actionlib
from std_srvs.srv import Trigger, TriggerRequest
from sensor_msgs.msg import LaserScan 
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Twist
from time import sleep
from nav_msgs.msg import Odometry
from basics_exam.msg import record_odomAction, record_odomFeedback, record_odomResult, record_odomGoal

rospy.init_node("node_main_program")
move = Twist()

def feedback_callback(feedback):
    pass 

client = actionlib.SimpleActionClient("/rec_odom_as", record_odomAction)
client.wait_for_server()

goal = record_odomGoal()
client.send_goal(goal, feedback_cb = feedback_callback)

sleep(2)

rospy.wait_for_service("/crash_direction_service")
my_service = rospy.ServiceProxy("/crash_direction_service", Trigger)
my_service_obj = TriggerRequest()
result = my_service(my_service_obj)
print result

### 

def move_right():
    move.linear.x = 0.5
    move.angular.z = -0.5
    pub.publish(move)

def move_left():
    move.linear.x = 0.5
    move.angular.z = 0.5 
    pub.publish(move)

def move_front():
    move.linear.x = 0.5
    move.angular.z = 0.0 
    pub.publish(move)

def stop():
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)

def callback(msg):
    # for t in xrange(0, 60):
    #     mess = result.message
    #     if mess == "right":
    #         move_right()
    #         # sleep(1)
    #     elif mess == "left":
    #         move_left()
    #         # sleep(1)
    #     elif mess == "front":
    #         move_front()
    #         # sleep(1)
    # stop()
    # sleep(1)
    
    for r in xrange (0, 5):
        move.linear.x = 1
        move.angular.z = -0.45
        # sleep(1)
        pub.publish(move)
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    sleep(1)

pub = rospy.Publisher("/husky_velocity_controller/cmd_vel", Twist, queue_size=1) # publisher
sub = rospy.Subscriber("/camera/scan", LaserScan, callback) # subscriber
move = Twist()
rospy.spin()


client.wait_for_result()
action_result = client.get_result()
print("Pose:")
print action_result.result_odom_array