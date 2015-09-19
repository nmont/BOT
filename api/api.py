__author__ = 'Ben Williams'

import Instruction
import InstructionList

LEFT_BUMPER_START = 10
LEFT_BUMPER_END = 11
RIGHT_BUMPER_START = 12
RIGHT_BUMPER_END = 13


# Takes in string file name
# outputs fulled constructed instruction list
def txt_to_instruction_list(file_name):
    f = open(file_name, 'r')
    i = InstructionList()
    for line in f:
        instruction = parse_instruction(line)
        i.append_instruction(instruction)
    return i


# TODO - Implement lookup for instruction numbers
def parse_instruction(string):
    i = Instruction(int(string))
    return i
