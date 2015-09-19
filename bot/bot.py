__author__ = 'ben'

# TODO - Run these before this script compiles
import sys
sys.path.append('/home/ben/workspace/BOT/api')

import api

def Record():
    temp_file = open("temp.json", "w")
    api.set_led(api.PROGRAM_LED_ID, api.RED)
    print "Record"

def Play():
    print "Play"

while True:
    if api.get_prog_switch():
        Record()
    else:
        Play()

