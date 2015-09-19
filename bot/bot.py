__author__ = 'ben'

import sys
sys.path.append('/home/ben/workspace/BOT/api')

import api

program_mode = api.get_prog_switch()

while True:
    if api.get_prog_switch():
        Record()
    else:
        Play()

def Record():
    print "Record"

def Play():
    print "Play"

