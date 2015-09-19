__author__ = 'ben'

import api
import InstructionList

instructions = InstructionList.InstructionList()
instructions.append_instruction(15)
instructions.append_instruction(16)
instructions.append_instruction(17)
instructions.append_instruction(18)
instructions.append_instruction(19)

api.instruction_list_to_json(instructions, "test_json.json")
