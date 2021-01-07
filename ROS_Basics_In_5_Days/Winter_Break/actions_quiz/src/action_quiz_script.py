#! /usr/bin/env python

import rospy
import actionlib
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult
from std_msgs.msg import Empty

class ActionQuizClass(object):
    _feedback = CustomActionMsgFeedback
    _result = CustomActionMsgResult

    def __init__(self):
        self._as = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
        self._as.start() 
    
    def goal_callback(self, goal):
        success = True

        self.pub_takeoff = rospy.Publisher("/drone/takeoff", Empty, queue_size=1)
        while self.pub_takeoff.get_num_connections() < 1:
            rospy.sleep(1)

        self.pub_land = rospy.Publisher("/drone/land", Empty, queue_size=1)
        while self.pub_land.get_num_connections() < 1:
            rospy.sleep(1)

        self.command = goal.goal

        if self._as.is_preempt_requested():
            rospy.loginfo("Goal canceled/preemped")
            self._as.set_preempted()
            success = False
            rospy.loginfo("ACTION FAILED")
            quit()

        if (self.command == "TAKEOFF"):
            rospy.loginfo("Taking off ...")
            self.pub_takeoff.publish(Empty())
            rospy.sleep(3)
            rospy.loginfo("Took off!")
        
        if (self.command == "LAND"):
            rospy.loginfo("Landing ...")
            self.pub_land.publish(Empty())
            rospy.sleep(3)
            rospy.loginfo("Landed!")
        
        if success:
            rospy.loginfo("ACTION SUCCESS")


if __name__ == "__main__":
    rospy.init_node("node_action_quiz_script")
    ActionQuizClass()
    rospy.spin()
