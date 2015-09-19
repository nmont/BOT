__author__ = 'Ben Williams'

import InstructionList
import json

# Dependencies on Raspberry pi
import RPi.GPIO as GPIO

# INSTRUCTION IDS
MOVE_FORWARD = 1
PIVOT_LEFT = 2
PIVOT_RIGHT = 3
MOVE_BACKWARDS = 4
GOTO_START = 5
BEEP = 6
LEFT_BUMPER_START = 7
LEFT_BUMPER_END = 8
RIGHT_BUMPER_START = 9
RIGHT_BUMPER_END = 10
HALT_1S = 11
LED = 12
DONE = 13
DANCE = 14

# INTERRUPT IDS
GO_BUTTON_INTERRUPT = 20
LEFT_BUMPER_INTERRUPT = 21
RIGHT_BUMPER_INTERRUPT = 22

# GPIO_IDs
PROGRAM_LED_ID = 10
PROGRAM_SWITCH_ID = 19
GO_BUTTON_ID = 5
PROGRAM_BUZZER_ID = 21
WHEEL_BA = 16
WHEEL_AA = 13
WHEEL_BB = 12
WHEEL_AB = 6

# COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


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
    instruction = int(nfc)
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
    return 1


# TODO - Asynchronously read a value from NFC
def read_nfc():
    return None


# TODO - Decode instruction to its rgb tuple
def instruction_to_color(instruction_id):
    return 1


# TODO - Determine what to do based off instruction id
def do_instruction(instruction_id):
    return 1