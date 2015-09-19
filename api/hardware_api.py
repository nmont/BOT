import time
import RPi.GPIO as GPIO
import nxppy
import api


def init():

    # Set GPIO mode to BCM and and set each pin to input or output
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

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
def move(direction, move_time):

    time_counter = 0

    if direction == 'forward':
        # Left wheel forward
        GPIO.output(6, False)
        GPIO.output(13, True)

        # Right wheel forward
        GPIO.output(16, False)
        GPIO.output(12, True)

    if direction == 'backward':
        # Left wheel backward
        GPIO.output(6, True)
        GPIO.output(13, False)

        # Right wheel backward
        GPIO.output(16, True)
        GPIO.output(12, False)

    if direction == 'Right':
        # Left wheel backward
        GPIO.output(6, True)
        GPIO.output(13, False)

        # Right wheel backward
        GPIO.output(16, True)
        GPIO.output(12, False)

    if direction == 'backward':
        # Left wheel backward
        GPIO.output(6, True)
        GPIO.output(13, False)

        # Right wheel backward
        GPIO.output(16, True)
        GPIO.output(12, False)

    while time_counter < move_time:
        if GPIO.input(4) == 1:
            return api.GO_BUTTON_INTERRUPT

        time_counter += 50
        time.sleep(.05)

    # stop all wheels
    GPIO.output(6, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(16, False)


def get_nfc():
    mifare = nxppy.Mifare()
    try:
        uid = mifare.select()
        return uid
    except nxppy.SelectError:
        return None



