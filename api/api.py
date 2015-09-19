__author__ = 'Ben Williams'

import Instruction
import InstructionList

LEFT_BUMPER_START = 10
LEFT_BUMPER_END = 11
RIGHT_BUMPER_START = 12
RIGHT_BUMPER_END = 13

def txt_to_instruction_list(file):
    f = open(file, 'r')
    i = InstructionList()
    for line in f:
        instruction = parseInstruction(line)
        i.append_instruction(instruction)

def parseInstruction(string):
    i = Instruction(int(string))
    return i