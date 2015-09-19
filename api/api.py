__author__ = 'Ben Williams'

import InstructionList
import json


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

# GPIO_IDs
PROGRAM_LED_ID = 10
PROGRAM_SWITCH_ID = 4
GO_BUTTON_ID = 8
PROGRAM_BUZZER_ID = 7

# COLORS
RED = (255, 0, 0)


# Takes in string file name
# outputs fulled constructed instruction list
# TODO - Get this to work
def json_dict_to_instruction_list(json_dict):
    instructions = InstructionList.InstructionList()
    for key, val in json_dict.iteritems():
        if val is None:
            instructions.__dict__[key] = val
        elif isinstance(val, dict):
            instructions.__dict__[key] = json_dict_to_instruction_list(val)
        else:
            instructions.__dict__[key] = val
    print instruction_list_to_json(instructions)
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


"""class InstructionListDecoder(json.JSONDecoder):
    def default(self, o):
        if not isinstance(o, InstructionList.InstructionList):
            return super(InstructionListDecoder, self).default(o)
        else:
            return o.__dict__"""

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