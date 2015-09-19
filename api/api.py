__author__ = 'Ben Williams'

import InstructionList
import json

LEFT_BUMPER_START = 10
LEFT_BUMPER_END = 11
RIGHT_BUMPER_START = 12
RIGHT_BUMPER_END = 13


# Takes in string file name
# outputs fulled constructed instruction list
def json_to_instruction_list(file_name):
    f = open(file_name, 'r')
    instructions = InstructionList.InstructionList()
    json_list = json.load(f)
    print json_list


# TODO - Implement lookup for instruction numbers
def parse_instruction(string):
    instruction = int(string)
    return instruction


def instruction_list_to_json(instructions, file_name):
    f = open(file_name, 'w')
    # f.write(json.dumps(instructions))
    print json.dumps(instructions.__dict__)
    # print json.dumps(instructions.left_bumper)
    # print json.dumps(instructions.right_bumper)
    return 0

