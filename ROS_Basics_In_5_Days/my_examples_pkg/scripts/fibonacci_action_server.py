#! /usr/bin/env python
import rospy
import actionlib
from actionlib_tutorials.msg import FibonacciFeedback, FibonacciResult, FibonacciAction

class FibonacciClass(object):
    _feedback = FibonacciFeedback()
    _result = FibonacciResult()