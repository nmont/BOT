__author__ = 'ben'

import api
import InstructionList

instructions = InstructionList.InstructionList()
instructions.append_instruction(api.MOVE_FORWARD)
instructions.append_instruction(api.LEFT_BUMPER_START)
instructions.append_instruction(api.MOVE_BACKWARDS)
instructions.append_instruction(api.PIVOT_RIGHT)
instructions.append_instruction(api.LEFT_BUMPER_END)
instructions.append_instruction(api.BEEP)
instructions.append_instruction(api.RIGHT_BUMPER_START)
instructions.append_instruction(api.DONE)
instructions.append_instruction(api.RIGHT_BUMPER_END)
instructions.append_instruction(api.GOTO_START)

api.instruction_list_to_json(instructions)
# api.json_to_instruction_list(json_string)
