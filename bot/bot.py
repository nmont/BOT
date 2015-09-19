__author__ = 'ben'

# TODO - Run these before this script compiles
import sys
sys.path.append('/home/ben/workspace/BOT/api')

import api
import InstructionList

def Record():

    api.set_led(api.PROGRAM_LED_ID, api.RED)
    instructions = InstructionList.InstructionList()

    # While we are set to record state and the user hasn't finalized the program
    while api.read_gpio(api.PROGRAM_SWITCH_ID) and not api.read_gpio(api.GO_BUTTON_ID):
        nfc = api.read_nfc()
        if nfc != None:
            instructions.append_instruction(api.parse_instruction(nfc))
            # buzz the buzzer
            api.set_gpio(api.PROGRAM_BUZZER_ID)

    print "Record"

def Play():
    print "Play"

while True:
    if api.read_gpio(api.PROGRAM_SWITCH_ID):
        Record()
    else:
        Play()

