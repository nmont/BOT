import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# A-B
GPIO.setup(6, GPIO.OUT)

# A-A
GPIO.setup(13, GPIO.OUT)

# Set GPIO pin 6 (A-B) on and pin 13 (A-A) off
GPIO.output(6, True)
GPIO.output(13, False)

time.sleep(1)

# Set GPIO Pin 6 (A-B) back off
GPIO.output(6, False)
