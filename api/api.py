__author__ = 'Ben Williams'

import InstructionList
import json
import hardware_api
import time

# Dependencies on Raspberry pi
import RPi.GPIO as GPIO

# INSTRUCTION IDS
MOVE_FORWARD1 = 0x0438A55AA34081
MOVE_FORWARD2 = 0x042CA35AA34080
PIVOT_LEFT = 0x04C5865AA34080
PIVOT_RIGHT = 0x045F855AA34080
MOVE_BACKWARDS1 = 0x04F9A05AA34080
MOVE_BACKWARDS2 = 0x041DA45AA34080
GOTO_START = 0x043C9F5AA34080
BEEP = 0x0454A55AA34080
LEFT_BUMPER_START = 0x041E865AA34080
LEFT_BUMPER_END = 0x04D7995AA34080
RIGHT_BUMPER_START = 0x042CA35AA34080
RIGHT_BUMPER_END = 0x0474A05AA34081
HALT_1S = 0x047FA05AA34080
LED = 0x04A0865AA34080
DONE = 0x04759F5AA34081
DANCE = 0x0429A45AA34080

# INTERRUPT IDS
GO_BUTTON_INTERRUPT = 20
LEFT_BUMPER_INTERRUPT = 21
RIGHT_BUMPER_INTERRUPT = 22
SWITCH_STATE_INTERRUPT = 23
SUCCESS = 1

# GPIO_IDs
PROGRAM_SWITCH_ID = 19
GO_BUTTON_ID = 5
PROGRAM_BUZZER_ID = 21
WHEEL_BA = 16
WHEEL_AA = 13
WHEEL_BB = 12
WHEEL_AB = 6
LEFT_BUMPER_ID = 20
RIGHT_BUMPER_ID = 26
RED_LED_ID = 22
GREEN_LED_ID = 17
RAINBOW_LED_ID = 27

# COLORS
RED = (4095, 0, 0)
GREEN = (0, 4095, 0)
BLUE = (0, 0, 4095)

# LED IDS
PROGRAM_LED_ID = 0
INSTRUCTION_LED_ID = 1

# Takes in string file name
# outputs fulled constructed instruction list
def json_dict_to_instruction_list(json_dict):
    instructions = InstructionList.InstructionList()
    for key, val in json_dict.iteritems():
        if val is None:
            instructions.__dict__[key] = val
        elif isinstance(val, dict):
            instructions.__dict__[key] = json_dict_to_instruction_list(val)
        else:
            instructions.__dict__[key] = val
    return instructions


# TODO - Implement lookup for instruction numbers
def parse_instruction(nfc):
    instruction = int(nfc,16)
    return instruction


def instruction_list_to_json(instructions):
    return json.dumps(instructions, cls=InstructionListEncoder)


class InstructionListEncoder(json.JSONEncoder):
    def default(self, o):
        if not isinstance(o, InstructionList.InstructionList):
            return super(InstructionListEncoder, self).default(o)
        else:
            return o.__dict__


# TODO - Read in state
def read_gpio(gpio_id):
    return 1


# TODO - Set state
def set_gpio(gpio_id):
    return 1


# TODO - Set LED based off of ID and RGB combination
def set_led(led_id, color):
    # Open up i2c com with pwm driver


    # set R led_id low start address to 0
    # set R led_id high start address to 0
    # set G led_id low start address to 0
    # set G led_id high start address to 0
    # set B led_id low start address to 0
    # set B led_id high start address to 0

    # set R led_id low end address to color[0] & 0x0FF
    # set R led_id high end address to (color[0] >> 8) & 0x0F

    # set G led_id low end address to color[1] & 0x0FF
    # set G led_id high end address to (color[1] >> 8) & 0x0F

    # set B led_id low end address to color[2] & 0x0FF
    # set B led_id high end address to (color[2] >> 8) & 0x0F

    # close i2c com

    return 1


# TODO - Asynchronously read a value from NFC
def read_nfc():
    return None


# TODO - Decode instruction to its rgb tuple
def instruction_to_color(instruction_id):
    return 1


# TODO - Determine what to do based off instruction id
def do_instruction(instruction_id):
    if instruction_id == MOVE_FORWARD1 or instruction_id == MOVE_FORWARD2:
        return hardware_api.move('forward', 1000)
    elif instruction_id == PIVOT_LEFT:
        return hardware_api.move('left', 1000)
    elif instruction_id == PIVOT_RIGHT:
        return hardware_api.move('right', 1000)
    elif instruction_id == MOVE_BACKWARDS1 or instruction_id == MOVE_BACKWARDS2:
        return hardware_api.move('backward', 1000)
    elif instruction_id == BEEP:
        return hardware_api.beep()
    elif instruction_id == HALT_1S:
        time.sleep(1)
        return SUCCESS
    elif instruction_id == LED:
        hardware_api.blink()
        return SUCCESS
    elif instruction_id == DANCE:
        hardware_api.dance()
        return
    else:
        return
