#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan 
from time import sleep

class Maze(object):

    def __init__(self):
        
        # odom subscriber
        self.my_Odom_Sub = rospy.Subscriber("/odom", Odometry, self.callback_odom)
        self.odom_msg = Odometry()

        rospy.sleep(1)

        # laser subscriber
        self.my_laser_sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, self.callback_laser)
        self.laser_msg = LaserScan()

        # service init
        self.my_service = rospy.Service("turtlebot_maze_service_server", Trigger, self.callback_serv)

        # subscriber
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        while self.pub.get_num_connections() < 1:
            sleep(1)
        self.move = Twist()

    def callback_serv(self, request):
        self.response = TriggerResponse()
        self.response.success = False
        self.response.message = "Not successfull" 
        reached_end = False
        
        while not reached_end:
            front = self.get_laser_front()
            # back = self.get_laser_back()
            left = self.get_laser_left()
            right = self.get_laser_right()
            print("front = ", front)
            # print("back = ", back)
            print("left = ", left)
            print("right = ", right)

            while (front >= 2):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                print("front = ", front)
                print("left = ", left)
                print("right = ", right)
                if (front > 6 and left > 6 and right > 6):
                    reached_end = True 
                    break
                self.move_forward_fast()
            
            while (front < 1.5 and front > 0.8):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                print("front = ", front)
                print("left = ", left)
                print("right = ", right)
                self.move_forward_slow()
                sleep(0.5)
                self.stop_moving()
            

            if (front < 0.8 and right > left):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                print("front = ", front)
                print("left = ", left)
                print("right = ", right)
                self.turn_right()

            elif (front < 0.8 and right < left):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                print("front = ", front)
                print("left = ", left)
                print("right = ", right)
                self.turn_left()
            
            elif (front < 0.2):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                print("front = ", front)
                print("left = ", left)
                print("right = ", right)
                self.back_up()
                
        if reached_end:
            self.stop_moving()
            rospy.loginfo("END OF MAZE REACHED")
            self.response.success = True
            self.response.message = "Successfull Movement" 

        return self.response

    def turn_left(self):
        front = self.get_laser_front()
        print("front = ", front)
        while (front < 2.95):
            print("front = ", front)
            rospy.loginfo("Turning left")
            self.move.linear.x = 0
            self.move.angular.z = 0.3
            self.pub.publish(self.move)
            front = self.get_laser_front()
            sleep(0.1)

    def turn_right(self):
        front = self.get_laser_front()
        print("front = ", front)
        while (front < 2.95):
            print("front = ", front)
            rospy.loginfo("Turning right")
            self.move.linear.x = 0
            self.move.angular.z = -0.3
            self.pub.publish(self.move)
            front = self.get_laser_front()
            sleep(0.1)

    def move_forward_fast(self):
        rospy.loginfo("Moving Forward")
        self.move.linear.x = 0.5
        self.move.angular.z = 0
        self.pub.publish(self.move)
    
    def move_forward_slow(self):
        rospy.loginfo("Moving Forward")
        self.move.linear.x = 0.25
        self.move.angular.z = 0
        self.pub.publish(self.move)
    
    def stop_moving(self):
        rospy.loginfo("Stopping!")
        self.move.linear.x = 0
        self.move.angular.z = 0
        self.pub.publish(self.move)

    def back_up(self):
        rospy.loginfo("Backing up:")
        self.move.linear.x = -0.2
        self.move.angular.z = 0
        self.pub.publish(self.move)
        sleep(0.5)

    def callback_odom(self, msg):
        self.odom_msg = msg

    def get_odom(self):
        sleep(0.3)
        return self.odom_msg

    def callback_laser(self, msg):
        self.laser_msg = msg

    def get_laser_front(self):
        sleep(0.08)
        return self.laser_msg.ranges[360]

    def get_laser_right(self):
        sleep(0.08)
        return self.laser_msg.ranges[0]

    def get_laser_left(self):
        sleep(0.08)
        return self.laser_msg.ranges[719]

if __name__ == "__main__":
    rospy.init_node("node_turtlebot_maze_service_server")
    Maze()
    rospy.spin()