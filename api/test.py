__author__ = 'ben'

import api
import InstructionList
import json

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

f = open('test_json.json', 'w')

json_string = api.instruction_list_to_json(instructions)

f.write(json_string)
f.close()

api.json_dict_to_instruction_list(json.loads(json_string))
