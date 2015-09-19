import time
import RPi.GPIO as GPIO
import nxppy
import api


def init():

    # Set GPIO mode to BCM and and set each pin to input or output
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Wheel A-B
    GPIO.setup(api.WHEEL_AB, GPIO.OUT)
    GPIO.output(api.WHEEL_AB, False)

    # Wheel A-A
    GPIO.setup(api.WHEEL_AB, GPIO.OUT)
    GPIO.output(api.WHEEL_AA, False)

    # Wheel B-A
    GPIO.setup(api.WHEEL_BA, GPIO.OUT)
    GPIO.output(api.WHEEL_BA, False)

    # Buzzer
    GPIO.setup(api.PROGRAM_BUZZER_ID, GPIO.OUT)
    GPIO.output(api.PROGRAM_BUZZER_ID, False)

    # Push Button left and right, respectively
    GPIO.setup(api.LEFT_BUMPER_ID, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(api.RIGHT_BUMPER_ID, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Program switch
    GPIO.setup(api.PROGRAM_SWITCH_ID, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Go button
    GPIO.setup(api.GO_BUTTON_ID, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Move in a direction for a given time in MILLISECONS
def move(direction, move_time):

    time_counter = 0

    if direction == 'forward':
        # Left wheel forward
        GPIO.output(api.BUTTON_AB, False)
        GPIO.output(api.BUTTON_AA, True)

        # Right wheel forward
        GPIO.output(api.BUTTON_BA, False)
        GPIO.output(api.BUTTON_BB, True)

    if direction == 'backward':
        # Left wheel backward
        GPIO.output(api.BUTTON_AB, True)
        GPIO.output(api.BUTTON_AA, False)

        # Right wheel backward
        GPIO.output(api.BUTTON_BA, True)
        GPIO.output(api.BUTTON_BB, False)

    if direction == 'Right':
        # Left wheel backward
        GPIO.output(api.BUTTON_AB, True)
        GPIO.output(api.BUTTON_AA, False)

        # Right wheel backward
        GPIO.output(api.BUTTON_BA, True)
        GPIO.output(api.BUTTON_BB, False)

    if direction == 'backward':
        # Left wheel backward
        GPIO.output(api.BUTTON_AB, True)
        GPIO.output(api.BUTTON_AA, False)

        # Right wheel backward
        GPIO.output(api.BUTTON_BA, True)
        GPIO.output(api.BUTTON_BB, False)

    while time_counter < move_time:
        if GPIO.input(4) == 1:
            return api.GO_BUTTON_INTERRUPT

        time_counter += 50
        time.sleep(.05)

    # stop all wheels
    GPIO.output(api.BUTTON_AB, False)
    GPIO.output(api.BUTTON_BB, False)
    GPIO.output(api.BUTTON_AA, False)
    GPIO.output(api.BUTTON_BA, False)


def get_nfc():
    mifare = nxppy.Mifare()
    try:
        uid = mifare.select()
        return uid
    except nxppy.SelectError:
        return None



