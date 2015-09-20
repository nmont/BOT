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
    return decode_instruction_list(instructions)


def encode_instruction(nfc):
    if nfc == MOVE_FORWARD1 or nfc == MOVE_FORWARD2:
        return 1
    elif nfc == PIVOT_LEFT:
        return 2
    elif nfc == PIVOT_RIGHT:
        return 3
    elif nfc == MOVE_BACKWARDS1 or nfc == MOVE_BACKWARDS2:
        return 4
    elif nfc == BEEP:
        return 5
    elif nfc == HALT_1S:
        return 6
    elif nfc == LED:
        return 7
    elif nfc == DANCE:
        return 8
    elif nfc == LEFT_BUMPER_START:
        return 9
    elif nfc == LEFT_BUMPER_END:
        return 10
    elif nfc == RIGHT_BUMPER_START:
        return 11
    elif nfc == RIGHT_BUMPER_END:
        return 12
    elif nfc == GOTO_START:
        return 13
    elif nfc == DONE:
        return 14
    else:
        return -1


def decode_instruction(instruction_id):
    if instruction_id == 1:
        return MOVE_FORWARD1
    elif instruction_id == 2:
        return PIVOT_LEFT
    elif instruction_id == 3:
        return PIVOT_RIGHT
    elif instruction_id == 4:
        return MOVE_BACKWARDS1
    elif instruction_id == 5:
        return BEEP
    elif instruction_id == 6:
        return HALT_1S
    elif instruction_id == 7:
        return LED
    elif instruction_id == 8:
        return DANCE
    elif instruction_id == 9:
        return LEFT_BUMPER_START
    elif instruction_id == 10:
        return LEFT_BUMPER_END
    elif instruction_id == 11:
        return RIGHT_BUMPER_START
    elif instruction_id == 12:
        return RIGHT_BUMPER_END
    elif instruction_id == 13:
        return GOTO_START
    elif instruction_id == 14:
        return DONE
    else:
        return -1


def instruction_list_to_json(instructions):
    instructions = encode_instruction_list(instructions)
    output_string = json.dumps(instructions, cls=InstructionListEncoder)
    decode_instruction_list(instructions)
    return output_string


def encode_instruction_list(instructions):
    for i in xrange(len(instructions.main_list)):
        instructions.main_list[i] = encode_instruction(instructions.main_list[i])
    if instructions.left_bumper is not None:
        instructions.left_bumper = encode_instruction_list(instructions.left_bumper)
    if instructions.right_bumper is not None:
        instructions.right_bumper = encode_instruction_list(instructions.right_bumper)
    return instructions


def decode_instruction_list(instructions):
    for i in xrange(len(instructions.main_list)):
        instructions.main_list[i] = decode_instruction(instructions.main_list[i])
    if instructions.left_bumper is not None:
        instructions.left_bumper = decode_instruction(instructions.left_bumper)
    if instructions.right_bumper is not None:
        instructions.right_bumper = decode_instruction(instructions.right_bumper)
    return instructions

class InstructionListEncoder(json.JSONEncoder):
    def default(self, o):
        if not isinstance(o, InstructionList.InstructionList):
            return super(InstructionListEncoder, self).default(o)
        else:
            return o.__dict__


# TODO - Determine what to do based off instruction id
def do_instruction(instruction_id):
    if instruction_id == MOVE_FORWARD1 or instruction_id == MOVE_FORWARD2:
        return hardware_api.move('forward', 150)
    elif instruction_id == PIVOT_LEFT:
        return hardware_api.move('left', 150)
    elif instruction_id == PIVOT_RIGHT:
        return hardware_api.move('right', 500)
    elif instruction_id == MOVE_BACKWARDS1 or instruction_id == MOVE_BACKWARDS2:
        return hardware_api.move('backward', 500)
    elif instruction_id == BEEP:
        return hardware_api.beep()
    elif instruction_id == HALT_1S:
        time.sleep(1)
        return SUCCESS
    elif instruction_id == LED:
        hardware_api.blink_rainbow()
        return SUCCESS
    elif instruction_id == DANCE:
        hardware_api.dance()
        return
    else:
        return
