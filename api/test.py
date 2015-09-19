__author__ = 'ben'

import api
import InstructionList

instructions = InstructionList.InstructionList()
instructions.append_instruction(api.MOVE_FORWARD)
instructions.append_instruction(api.MOVE_FORWARD)
instructions.append_instruction(api.LEFT_BUMPER_START)
instructions.append_instruction(api.MOVE_BACKWARDS)
instructions.append_instruction(api.PIVOT_RIGHT)
instructions.append_instruction(api.LEFT_BUMPER_END)
instructions.append_instruction(api.MOVE_FORWARD)
instructions.append_instruction(api.GOTO_START)

json_string = ''

print api.instruction_list_to_json(instructions, json_string)
