#!/usr/bin/env python

from std_msgs.msg import String
from geometry_msgs.msg import Twist

import rospy
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module


factory = PiGPIOFactory(host='192.168.171.34')
led_green = LED(2, pin_factory=factory)
led_yellow = LED(4, pin_factory=factory)
led_red = LED(17, pin_factory=factory)
# led_white = LED(27, pin_factory=factory)
led_blue = LED(3, pin_factory=factory)

blinkrate = 0.2
# led_red.off()
# led_blue.off()
# led_green.off()
# led_yellow.off()

# below are settings for GPIO boardmode to run on RPI, do not run from remote PC
# GPIO.setwarnings(False)    # Ignore warning for now
# GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)    # Set pin 1,3,5,7 to be an output pin and set initial value to low (off)

linear_x = 0
rotation_z = 0

def shutdown():
    rospy.loginfo("Stop Blink")
    rate.sleep()

def callback(msg):
    # rospy.loginfo("Received a /cmd_vel message!")
    # rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    # rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
    global linear_x, rotation_z
    
    linear_x = msg.linear.x
    rotation_z = msg.angular.z
    

    
def redblink():
    # print ("red blink")
    led_red.on()
    sleep(blinkrate)
    led_red.off()
    sleep(blinkrate)

def greenblink():
    print ("green blink")
    led_green.on()
    sleep(blinkrate)
    led_green.off()
    sleep(blinkrate)

def blueblink():
    # print ("blue blink")
    led_blue.on()
    sleep(blinkrate)
    led_blue.off()
    sleep(blinkrate)

def yellowblink():
    # print ("yellow blink")
    led_yellow.on()
    sleep(blinkrate)
    led_yellow.off()
    sleep(blinkrate)

def redyellowblink():
    # print ("red blink")
    led_red.on()
    led_yellow.on()
    sleep(blinkrate)
    led_red.off()
    led_yellow.off()
    sleep(blinkrate)

def redgreenblink():
    # print ("red blink")
    led_red.on()
    led_green.on()
    sleep(blinkrate)
    led_red.off()
    led_green.off()
    sleep(blinkrate)

def blueyellowblink():
    # print ("blue blink")
    led_blue.on()
    led_yellow.on()
    sleep(blinkrate)
    led_blue.off()
    led_yellow.off()
    sleep(blinkrate)

def bluegreenblink():
    # print ("blue blink")
    led_blue.on()
    led_green.on()
    sleep(blinkrate)
    led_blue.off()
    led_green.off()
    sleep(blinkrate)




# if __name__ == '__main__':
#     listener()

# def listener():

rospy.init_node('blink_directional', anonymous=True)
rospy.on_shutdown(shutdown)
rate = rospy.Rate(2) #rate of subscription or loop set at 1 per sec


while not rospy.is_shutdown():

    sub = rospy.Subscriber('cmd_vel', Twist, callback)
        # rospy.spin()
        # pub = rospy.Publisher('turtle1/command_velocity',Velocity)

    # print ('x is ' + str(linear_x))
    # print ('z is ' + str(rotation_z))
    

    if linear_x > 0.0 and rotation_z == 0.0:
        redblink()
    elif linear_x > 0.0 and rotation_z > 0.0:
        redyellowblink()
        
    elif linear_x > 0.0 and rotation_z < 0.0:
        redgreenblink()
        
    elif linear_x < 0.0 and rotation_z == 0.0:
        blueblink()
    elif linear_x < 0.0 and rotation_z > 0.0:
        bluegreenblink()
        
    elif linear_x < 0.0 and rotation_z < 0.0:
        blueyellowblink()
        
    elif rotation_z > 0.0 and linear_x == 0.0:
        yellowblink()
    elif rotation_z < 0.0 and linear_x == 0.0:
        greenblink()
    else:
        # print ("all off")
        led_red.off()
        led_blue.off()
        led_green.off()
        led_yellow.off()
        
    
    rate.sleep()

rospy.spin()