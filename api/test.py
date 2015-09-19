__author__ = 'ben'

import api
import InstructionList
import Instruction

instructions = InstructionList.InstructionList()
instr = Instruction.Instruction(15)
instructions.append_instruction(instr)
instructions.append_instruction(Instruction.Instruction(16))
instructions.append_instruction(Instruction.Instruction(17))
instructions.append_instruction(Instruction.Instruction(18))
instructions.append_instruction(Instruction.Instruction(19))

for instruction in instructions.main_list:
    print instruction.toString()

api.instruction_list_to_json(instructions, "test_json.json")
