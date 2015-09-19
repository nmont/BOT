__author__ = 'Ben Williams'

import Instruction
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
    instruction = Instruction.Instruction(int(string))
    return instruction


def instruction_list_to_json(instructions, file_name):
    if type(instructions) != InstructionList:
        return -1
    f = open(file_name, 'w')
    f.write(json.dump(instructions))
    print json.dump(instructions)
    return 0

