__author__ = 'Ben Williams'

import InstructionList
import json

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


# Takes in string file name
# outputs fulled constructed instruction list
def json_to_instruction_list(json_string):
    instructions = InstructionList.InstructionList()
    json_list = json.loads(json_string)
    print json_list


# TODO - Implement lookup for instruction numbers
def parse_instruction(string):
    instruction = int(string)
    return instruction


def instruction_list_to_json(instructions, output_string):
    output_string += '{\n"main":' + str(instructions.main_list) + ',\n'
    output_string += '"left": '
    if instructions.left_bumper is not None:
        output_string = instruction_list_to_json(instructions.left_bumper, output_string)
    else:
        output_string += '{}'
    output_string += ',\n'
    output_string += '"right": '
    if instructions.right_bumper is not None:
        output_string = instruction_list_to_json(instructions.right_bumper, output_string)
    else:
        output_string += '{}'
    output_string += ',\n'
    output_string += '}'
    return output_string
