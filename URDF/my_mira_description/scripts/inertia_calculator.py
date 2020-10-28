#! /usr/bin/env python

import math

class InertialCalculator(object):
    
    def __init__(self):
        print "InertialCalculator initialised ..."
    
    def start_ask_loop(self):
        selection = "START"

        while selection != "Q":
            print "################"
            print "Select Geometry to Calculate:"
            print "[1]Box width(w)*depth(d)*height(h)"
            print "[2]Sphere radius(r)"
            print "[3]Cylinder radius(r)*height(h)"
            print "[Q]END program"
            selection = raw_input(">>")
            self.select_action(selection)