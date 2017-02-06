#!/usr/bin/env python
import rospy
import actionlib
import random
import sys
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionGoal 
from actionlib_msgs.msg import *
import time

def DestNav(x,y):
    mvbs = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    mvbs.wait_for_server()
    rospy.loginfo("server ready")
    dest = MoveBaseGoal()
        
    dest.target_pose.header.frame_id = "map"
    dest.target_pose.header.stamp = rospy.Time.now()

    dest.target_pose.pose.position.x = x
    dest.target_pose.pose.position.y = y
    dest.target_pose.pose.position.z = 0
    dest.target_pose.pose.orientation.x = 0.0
    dest.target_pose.pose.orientation.y = 0.0
    dest.target_pose.pose.orientation.z = 0.0
    dest.target_pose.pose.orientation.w = 1.0
       
    rospy.loginfo("Sending goal location ...")
    mvbs.send_goal(dest)
            
            
    mvbs.wait_for_result(rospy.Duration(150))


if __name__ == "__main__":
    try:
        rospy.init_node("test_random")
        DestNav(6.7, 6.7)
	DestNav(3, -4)
	DestNav(6.7, 6.7)
	DestNav(-5, 8)
        DestNav(-3, 3)
	DestNav(-7.2,-4.36)
        DestNav(6, -8)

    except rospy.ROSInterruptException:
	pass
