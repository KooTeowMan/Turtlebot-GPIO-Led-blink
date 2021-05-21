from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

factory = PiGPIOFactory(host='192.168.104.34')
led_green = LED(2, pin_factory=factory)
led_yellow = LED(4, pin_factory=factory)
led_red = LED(17, pin_factory=factory)
led_white = LED(27, pin_factory=factory)
led_blue = LED(3, pin_factory=factory)

# GPIO.setwarnings(False)    # Ignore warning for now
# GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) 
# GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) 
# GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)    # Set pin 12,11,3,5,7 to be an output pin and set initial value to low (off)

rate = 0.05

while True: # Run forever
    led_green.on()
    led_yellow.on()
    led_red.on()
    led_white.on()
    led_blue.on()  
    sleep(rate)                  # Sleep 
    led_green.off()
    led_yellow.off()
    led_red.off()
    led_white.off()
    led_blue.off()  
    sleep(rate)                  # Sleep for 0.5  second



