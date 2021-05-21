#!/usr/bin/env python

import rospy
from std_msgs.msg import String
# from geometry_msgs.msg import Twist
# from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatusArray 
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

factory = PiGPIOFactory(host='192.168.148.34')

led_white = LED(27, pin_factory=factory)
blinkrate = 0.2

goal_state = 0

def shutdown():
	
	#rospy.loginfo("Stop TB3")
	#pub.publish(Twist())			#default Twist() has linear.x of 0 and angular.z of 0
	rate.sleep()

def callback(msg):
    global goal_state
    
    goal_state = msg.status_list[0].status
    
        
def whiteblink():
    led_white.on()
    sleep(blinkrate)
    led_white.off()
    sleep(blinkrate)
        
rospy.init_node('blink_goal', anonymous=True)			# Initiate a Node called 'blink'
rospy.on_shutdown(shutdown)
rate = rospy.Rate(1) #rate of subscription or loop set at 1 per sec

while not rospy.is_shutdown():
    
    sub = rospy.Subscriber('move_base/status', GoalStatusArray, callback)

    if goal_state == 3:
        whiteblink()
    else:
        led_white.off()
    
    rate.sleep()

rospy.spin()
