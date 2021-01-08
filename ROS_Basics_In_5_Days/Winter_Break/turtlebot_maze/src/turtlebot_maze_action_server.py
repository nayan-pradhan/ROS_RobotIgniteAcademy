#! /usr/bin/env python

import rospy
import actionlib
from turtlebot_maze.msg import MyTurtlebotMazeActionFeedback, MyTurtlebotMazeActionAction, MyTurtlebotMazeActionResult
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan 
from time import sleep
from std_srvs.srv import Trigger, TriggerResponse

class Maze(object):

    global reached_end_time
    reached_end_time = False
    global reached_end_maze 
    reached_end_maze = False
    global end_pos
    global init_pos

    _feedback = MyTurtlebotMazeActionFeedback()
    _result = MyTurtlebotMazeActionResult()

    def __init__(self):
        
        # odom subscriber
        self.my_Odom_Sub = rospy.Subscriber("/odom", Odometry, self.callback_odom)
        self.odom_msg = Odometry()

        rospy.sleep(1)

        # laser subscriber
        self.my_laser_sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, self.callback_laser)
        self.laser_msg = LaserScan()

        init_pos = self.get_odom()
        # print("init pos = ", init_pos)

        # service init
        self.my_service = rospy.Service("turtlebot_maze_service_server", Trigger, self.callback_serv)

        # action init
        self._as = actionlib.SimpleActionServer("turtlebot_maze_action_server", MyTurtlebotMazeActionAction, self.as_goal_callback, False)
        self._as.start()

        # publisher
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        while self.pub.get_num_connections() < 1:
            sleep(1)
        self.move = Twist()

    def as_goal_callback(self, goal):
        
        current_time = 0
        total_time_run = 120
        self.reached_end_time = False
        self.reached_end_maze = False

        arr = []

        while (current_time < total_time_run) and (not self.reached_end_maze):
            self.new_position = self.get_odom()

            x = self.new_position.pose.pose.position.x
            y = self.new_position.pose.pose.position.y
            z = self.new_position.pose.pose.position.z

            arr.append(x)
            arr.append(y)
    
            print (x,y,z)

            if (x < 1.5 and x > -1.5) and (y < -8.5):
                print (x,y,z)
                rospy.loginfo("END OF MAZE REACHED")
                self.stop_moving()
                self.reached_end_maze = True 

            # print("pos = ", self.new_position)
            current_time += 1
            sleep(1)

        if current_time == total_time_run:
            self.stop_moving()
            self.reached_end_time = True
            if (not self.reached_end_maze):
                rospy.loginfo("TIME UP. FAILED")
        
        if self.reached_end_maze:
            self.stop_moving()
            self._result.result_odom_array = arr
            self._as.set_succeeded(self._result)
            rospy.loginfo("Success")
                

    def callback_serv(self, request):

        self.response = TriggerResponse()
        self.response.success = False
        self.response.message = "Not successfull" 
        self.reached_end_maze = False
        self.reached_end_time = False
        
        while (not self.reached_end_maze) or (not self.reached_end_time):
            front = self.get_laser_front()
            left = self.get_laser_left()
            right = self.get_laser_right()
            # print("front = ", front)
            # print("left = ", left)
            # print("right = ", right)

            while (front >= 2):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                # print("front = ", front)
                # print("left = ", left)
                # print("right = ", right)
                if self.reached_end_maze:
                    self.stop_moving()
                    end_pos = self.get_odom()
                    # print("End pos = ", end_pos)
                    rospy.loginfo("END OF MAZE REACHED")
                    self.response.success = True
                    self.response.message = "Successfull Movement"
                    break
                # if ((front > 10 and left > 10 and right > 10) or (front > 10 and left > 10) or (left > 10 and right > 10) or (front > 10 and right > 10)):
                #     reached_end_maze = True 
                #     break

                self.move_forward_fast()
            
            while (front < 1.5 and front > 0.8):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                # print("front = ", front)
                # print("left = ", left)
                # print("right = ", right)
                self.move_forward_slow()
                sleep(0.5)
                self.stop_moving()
            

            if (front < 0.8 and right > left):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                # print("front = ", front)
                # print("left = ", left)
                # print("right = ", right)
                self.turn_right()

            elif (front < 0.8 and right < left):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                # print("front = ", front)
                # print("left = ", left)
                # print("right = ", right)
                self.turn_left()
            
            elif (front < 0.2):
                front = self.get_laser_front()
                left = self.get_laser_left()
                right = self.get_laser_right()
                # print("front = ", front)
                # print("left = ", left)
                # print("right = ", right)
                self.back_up()
            
            if self.reached_end_maze:
                self.stop_moving()
                end_pos = self.get_odom()
                # print("End pos = ", end_pos)
                rospy.loginfo("END OF MAZE REACHED")
                self.response.success = True
                self.response.message = "Successfull Movement"
                break
                    
        if self.reached_end_time:
            self.stop_moving()

        if self.reached_end_maze:
            self.stop_moving()
            end_pos = self.get_odom()
            # print("End pos = ", end_pos)
            rospy.loginfo("END OF MAZE REACHED")
            self.response.success = True
            self.response.message = "Successfull Movement" 

        return self.response

    def turn_left(self):
        front = self.get_laser_front()
        # print("front = ", front)
        while (front < 2.95):
            # print("front = ", front)
            # rospy.loginfo("Turning left")
            self.move.linear.x = 0
            self.move.angular.z = 0.3
            self.pub.publish(self.move)
            front = self.get_laser_front()
            sleep(0.1)

    def turn_right(self):
        front = self.get_laser_front()
        # print("front = ", front)
        while (front < 2.95):
            # print("front = ", front)
            # rospy.loginfo("Turning right")
            self.move.linear.x = 0
            self.move.angular.z = -0.3
            self.pub.publish(self.move)
            front = self.get_laser_front()
            sleep(0.1)

    def move_forward_fast(self):
        # rospy.loginfo("Moving Forward")
        self.move.linear.x = 1.0
        self.move.angular.z = 0
        self.pub.publish(self.move)
    
    def move_forward_slow(self):
        # rospy.loginfo("Moving Forward")
        self.move.linear.x = 0.25
        self.move.angular.z = 0
        self.pub.publish(self.move)
    
    def stop_moving(self):
        # rospy.loginfo("Stopping!")
        self.move.linear.x = 0
        self.move.angular.z = 0
        self.pub.publish(self.move)

    def back_up(self):
        # rospy.loginfo("Backing up:")
        self.move.linear.x = -0.2
        self.move.angular.z = 0
        self.pub.publish(self.move)
        sleep(0.5)

    def callback_odom(self, msg):
        self.odom_msg = msg

    def get_odom(self):
        sleep(0.1)
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
    rospy.init_node("node_turtlebot_maze_action_server")
    Maze()