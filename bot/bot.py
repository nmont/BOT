__author__ = 'ben'

import sys
sys.path.append('/home/ben/workspace/BOT/api')

import api
import InstructionList


def record():

    api.set_led(api.PROGRAM_LED_ID, api.RED)
    instructions = InstructionList.InstructionList()

    last_nfc = None

    # While we are set to record state and the user hasn't finalized the program
    while api.read_gpio(api.PROGRAM_SWITCH_ID):
        nfc = api.read_nfc()

        if last_nfc is not None and last_nfc == nfc:
            continue
        elif nfc is not None:
            instruction_id = api.parse_instruction(nfc)
            instructions.append_instruction(instruction_id)

            # buzz the buzzer
            api.set_gpio(api.PROGRAM_BUZZER_ID)
            color = api.instruction_to_color(instruction_id)

            # Set the instruction led to our desired color
            api.set_led(api.INSTRUCTION_LED_ID, color)
            last_nfc = nfc

        if api.read_gpio(api.GO_BUTTON_ID):
            # Overwrite instruction file
            f = open('instructions.json', 'w')
            f.write(api.instruction_list_to_json(instructions))
            f.close()
            break


def play():
    print "Play"

while True:
    if api.read_gpio(api.PROGRAM_SWITCH_ID):
        record()
    else:
        play()

