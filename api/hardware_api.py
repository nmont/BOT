import time
import RPi.GPIO as GPIO
import nxppy

def init():

        # Set GPIO mode to BCM and and set each pin to input or output
        GPIO.setmode(GPIO.BCM)

        # Wheel A-B
        GPIO.setup(6, GPIO.OUT)

        # Wheel A-A
        GPIO.setup(13, GPIO.OUT)

        # Wheel B-A
        GPIO.setup(16, GPIO.OUT)

        # Buzzer
        GPIO.setup(21, GPIO.OUT)


        # Push Button left and right, respectively
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Program switch
        GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Go button
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Move in a direction for a given time in MILLISECONS
def move(direction, time):

        if direction == 'right':
            GPIO.output(6, False)
            GPIO.output(13, True)
            if GPIO.input(4) == 1:
                // TODO Return Value
            time.sleep(time / 1000)


