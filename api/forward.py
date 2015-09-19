import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# A-B
GPIO.setup(6, GPIO.OUT)

# A-A
GPIO.setup(13, GPIO.OUT)

# Set GPIO pin 13 (A-A) on and pin 6 (A-B) off
GPIO.output(6, False)
GPIO.output(13, True)

time.sleep(1)

# Set GPIO Pin 13 (A-A) back off
GPIO.output(6, False)

