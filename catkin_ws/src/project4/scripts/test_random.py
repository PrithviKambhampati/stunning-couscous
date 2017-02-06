#!/usr/bin/env python
import rospy
import random
import sys
from move_base_msgs.msg import MoveBaseActionGoal 
import time


if __name__ == "__main__":
    try:
    	rospy.init_node("test_random")
    	rate = rospy.Rate(0.1)
	seq=0
        pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)
        cord=MoveBaseActionGoal()
        cord.header.seq=seq
        cord.header.stamp=rospy.Time.now()
        cord.goal.target_pose.header.seq=seq
        cord.goal.target_pose.header.stamp=rospy.Time.now()
        cord.goal.target_pose.header.frame_id="map"
        cord.goal.target_pose.pose.position.x=5
        cord.goal.target_pose.pose.position.y=3
        cord.goal.target_pose.pose.orientation.w=1.0
        pub.publish(cord)
        seq=seq+1
        rate.sleep()

	init_time=rospy.Time.now().secs
	while not rospy.is_shutdown() :
		if rospy.Time.now().secs-init_time<600:
    			pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)
			cord=MoveBaseActionGoal()
			cord.header.seq=seq
			cord.header.stamp=rospy.Time.now()
			cord.goal.target_pose.header.seq=seq
			cord.goal.target_pose.header.stamp=rospy.Time.now()
			cord.goal.target_pose.header.frame_id="map"
			x=7
			y=4
			cord.goal.target_pose.pose.position.x=x
			cord.goal.target_pose.pose.position.y=y
			cord.goal.target_pose.pose.orientation.w=1.0
			pub.publish(cord)
			seq=seq+1
		else:
			print "Time out for scanning. time now=%s initial time=%s" %(rospy.Time.now().secs,init_time)
			break
		print "random position selected x=%s y=%s" %(x,y)	
	   	rate.sleep()
	    
    except rospy.ROSInterruptException:
	pass
