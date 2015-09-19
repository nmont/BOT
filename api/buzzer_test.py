import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# A-A
GPIO.setup(4, GPIO.OUT)

# Set GPIO pin 4
GPIO.output(4, True)

time.sleep(.1)

# Set GPIO Pin 4 back off
GPIO.output(4, False)

