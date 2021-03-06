import time
import RPi.GPIO as GPIO
import nxppy
import api
import random

def init():

    # Set GPIO mode to BCM and and set each pin to input or output
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Wheel A-B
    GPIO.setup(api.WHEEL_AB, GPIO.OUT)
    GPIO.output(api.WHEEL_AB, False)

    # Wheel A-A
    GPIO.setup(api.WHEEL_AA, GPIO.OUT)
    GPIO.output(api.WHEEL_AA, False)

    # Wheel B-A
    GPIO.setup(api.WHEEL_BA, GPIO.OUT)
    GPIO.output(api.WHEEL_BA, False)

    # Wheel B-B
    GPIO.setup(api.WHEEL_BB, GPIO.OUT)
    GPIO.output(api.WHEEL_BB, False)

    # Buzzer
    GPIO.setup(api.PROGRAM_BUZZER_ID, GPIO.OUT)
    GPIO.output(api.PROGRAM_BUZZER_ID, False)

    # Rainbow, Red, Yellow, and Green LEDs, respectively
    GPIO.setup(api.RAINBOW_LED_ID, GPIO.OUT)
    GPIO.output(api.RAINBOW_LED_ID, False)

    GPIO.setup(api.RED_LED_ID, GPIO.OUT)
    GPIO.output(api.RED_LED_ID, False)

    GPIO.setup(api.GREEN_LED_ID, GPIO.OUT)
    GPIO.output(api.GREEN_LED_ID, False)

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

        # Right wheel forward
        GPIO.output(api.WHEEL_AB, True)
        GPIO.output(api.WHEEL_AA, False)

        # Left wheel forward
        GPIO.output(api.WHEEL_BA, True)
        GPIO.output(api.WHEEL_BB, False)

    if direction == 'backward':

        # Right wheel backward
        GPIO.output(api.WHEEL_AB, False)
        GPIO.output(api.WHEEL_AA, True)

        # Left wheel backward
        GPIO.output(api.WHEEL_BA, False)
        GPIO.output(api.WHEEL_BB, True)

    if direction == 'right':
        turn_right()

    if direction == 'left':
        turn_left()

    while time_counter < move_time:
        if GPIO.input(api.GO_BUTTON_ID) == 1:
            stop_wheels()
            return api.GO_BUTTON_INTERRUPT
        elif GPIO.input(api.LEFT_BUMPER_ID) == 1:
            stop_wheels()
            return api.LEFT_BUMPER_INTERRUPT
        elif GPIO.input(api.RIGHT_BUMPER_ID) == 1:
            stop_wheels()
            return api.RIGHT_BUMPER_INTERRUPT
        elif GPIO.input(api.PROGRAM_SWITCH_ID) == 1:
            stop_wheels()
            return  api.SWITCH_STATE_INTERRUPT

        time_counter += 50
        time.sleep(.05)

    stop_wheels()
    return api.SUCCESS


def get_nfc():
    mifare = nxppy.Mifare()
    try:
        uid = mifare.select()
        return uid
    except nxppy.SelectError:
        return None

def beep():
    GPIO.output(api.PROGRAM_BUZZER_ID, True)
    time.sleep(.3)
    GPIO.output(api.PROGRAM_BUZZER_ID, False)
    return api.SUCCESS


def dance():
    seed = random.uniform(-1, 1)
    GPIO.output(api.RAINBOW_LED_ID, True)
    if seed < 0:
        turn_left()
        time.sleep(.25)
        stop_wheels()
        time.sleep(1.3)
        turn_right()
        time.sleep(.25)
        stop_wheels()
        time.sleep(1.9)
        beep()
        turn_left()
        time.sleep(.3)
        stop_wheels()
        time.sleep(1.3)
        blink_green()
    else:
        turn_right()
        time.sleep(.25)
        stop_wheels()
        time.sleep(1.3)
        turn_left()
        time.sleep(.25)
        stop_wheels()
        beep()
        time.sleep(1.9)
        blink_red()
        turn_right()
        time.sleep(.25)
        stop_wheels()
        time.sleep(1.3)

    stop_wheels()
    GPIO.output(api.RAINBOW_LED_ID, False)
    return api.SUCCESS

def turn_left():
    print 'turning left'
    # Left wheel backward
    GPIO.output(api.WHEEL_BA, False)
    GPIO.output(api.WHEEL_BB, True)

    # Right wheel forward
    GPIO.output(api.WHEEL_AB, True)
    GPIO.output(api.WHEEL_AA, False)

def turn_right():

    print 'turning right'
    # Left wheel forward
    GPIO.output(api.WHEEL_BA, True)
    GPIO.output(api.WHEEL_BB, False)

    # Right wheel backward
    GPIO.output(api.WHEEL_AB, False)
    GPIO.output(api.WHEEL_AA, True)

def stop_wheels():
    # stop all wheels
    GPIO.output(api.WHEEL_AB, False)
    GPIO.output(api.WHEEL_BB, False)
    GPIO.output(api.WHEEL_AA, False)
    GPIO.output(api.WHEEL_BA, False)

def blink_red():
    GPIO.output(api.RED_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.RED_LED_ID, False)
    time.sleep(.5)
    GPIO.output(api.RED_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.RED_LED_ID, False)
    return api.SUCCESS

def blink_green():
    GPIO.output(api.GREEN_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.GREEN_LED_ID, False)
    time.sleep(.5)
    GPIO.output(api.GREEN_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.GREEN_LED_ID, False)
    time.sleep(.5)
    GPIO.output(api.GREEN_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.GREEN_LED_ID, False)
    return api.SUCCESS

def blink_rainbow():
    GPIO.output(api.RAINBOW_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.RAINBOW_LED_ID, False)
    time.sleep(.5)
    GPIO.output(api.RAINBOW_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.RAINBOW_LED_ID, False)
    time.sleep(.5)
    GPIO.output(api.RAINBOW_LED_ID, True)
    time.sleep(.5)
    GPIO.output(api.RAINBOW_LED_ID, False)
    return api.SUCCESS

def halt(halt_time):
    counter_time = 0
    while(counter_time < halt_time):
        if GPIO.input(api.GO_BUTTON_ID) == 1:
            return api.GO_BUTTON_INTERRUPT
        elif GPIO.input(api.LEFT_BUMPER_ID) == 1:
            return api.LEFT_BUMPER_INTERRUPT
        elif GPIO.input(api.RIGHT_BUMPER_ID) == 1:
            return api.RIGHT_BUMPER_INTERRUPT
        elif GPIO.input(api.PROGRAM_SWITCH_ID) == 1:
            return  api.SWITCH_STATE_INTERRUPT

        counter_time += 50
        time.sleep(.05)

    return api.SUCCESS