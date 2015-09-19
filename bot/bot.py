__author__ = 'ben'

import sys
import json
sys.path.append('/home/pi/BOT/api')

import api
import hardware_api
import InstructionList
import RPi.GPIO as GPIO
import time

def bumper(instructions):
    print "Bumper"
    instruction_counter = 0
    while instruction_counter < len(instructions.main_list):
        instruction_id = instructions.main_list[instruction_counter]
        if instruction_id == api.GOTO_START:
            instruction_counter = 0
            continue
        elif instruction_id == api.DONE:
            break
        interrupt = api.do_instruction(instruction_id)
        if interrupt == api.GO_BUTTON_INTERRUPT:
            instruction_counter = 0
            continue
        elif interrupt == api.LEFT_BUMPER_INTERRUPT and instructions.left_bumper is not None:
            bumper(instructions.left_bumper)
        elif interrupt == api.RIGHT_BUMPER_INTERRUPT and instructions.right_bumper is not None:
            bumper(instructions.right_bumper)
        else:
            instruction_counter += 1


def record():

    api.set_led(api.PROGRAM_LED_ID, api.RED)
    instructions = InstructionList.InstructionList()

    last_nfc = None

    hardware_api.init()
    # While we are set to record state and the user hasn't finalized the program
    while GPIO.input(api.PROGRAM_SWITCH_ID) == 1 and not GPIO.input(api.GO_BUTTON_ID):
        print "Recording"
        nfc = hardware_api.get_nfc()
        if last_nfc is not None and last_nfc == nfc:
            continue
        elif nfc is not None:
            print "Appending Instruction"
            instruction_id = api.parse_instruction(nfc)
            instructions.append_instruction(instruction_id)

            # buzz the buzzer
            #api.set_gpio(api.PROGRAM_BUZZER_ID)
            GPIO.output(api.PROGRAM_BUZZER_ID, True)
            time.sleep(.1)
            GPIO.output(api.PROGRAM_BUZZER_ID, False)

            color = api.instruction_to_color(instruction_id)

            # Set the instruction led to our desired color
            api.set_led(api.INSTRUCTION_LED_ID, color)

        if GPIO.input(api.GO_BUTTON_ID) == 1:
            print "Programmed"
            GPIO.output(api.PROGRAM_BUZZER_ID, True)
            time.sleep(.3)
            GPIO.output(api.PROGRAM_BUZZER_ID, False)
            # Overwrite instruction file
            f = open('instructions.json', 'w')
            f.write(api.instruction_list_to_json(instructions))
            f.close()
            break

        last_nfc = nfc


def play():
    api.set_led(api.PROGRAM_LED_ID, api.GREEN)
    f = open('instructions.json', 'r')
    json_dict = json.loads(f.read())
    f.close()
    instructions = api.json_dict_to_instruction_list(json_dict)
    instruction_counter = 0
    print instruction_counter

    while instruction_counter < len(instructions.main_list):
        instruction_id = instructions.main_list[instruction_counter]
        print instruction_id
        if instruction_id == api.GOTO_START:
            instruction_counter = 0
            continue
        elif instruction_id == api.DONE:
            break
        interrupt = api.do_instruction(instruction_id)
        if interrupt == api.GO_BUTTON_INTERRUPT:
            instruction_counter = 0
            continue
        elif interrupt == api.LEFT_BUMPER_INTERRUPT and instructions.left_bumper is not None:
            bumper(instructions.left_bumper)
        elif interrupt == api.RIGHT_BUMPER_INTERRUPT and instructions.right_bumper is not None:
            bumper(instructions.right_bumper)
        else:
            instruction_counter += 1

    while not api.read_gpio(api.GO_BUTTON_ID) and not api.read_gpio(api.PROGRAM_SWITCH_ID):
        continue

while True:
    if GPIO.input(api.PROGRAM_SWITCH_ID) == 1:
        record()
    else:
        play()

