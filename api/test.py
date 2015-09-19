__author__ = 'ben'

import api
import InstructionList
import Instruction

instructions = InstructionList.InstructionList()
instructions.append_instruction(Instruction.Instruction(15))
instructions.append_instruction(Instruction.Instruction(16))
instructions.append_instruction(Instruction.Instruction(17))
instructions.append_instruction(Instruction.Instruction(18))
instructions.append_instruction(Instruction.Instruction(19))

print instructions

api.instruction_list_to_json(instructions, "test_json.json")
