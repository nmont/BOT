__author__ = 'Ben Williams'

import api

class Instruction:
    # The interface for defining all B.O.T. instructions

    INSTRUCTION_ID = 0

    def __init__(self, _id):
        self.INSTRUCTION_ID = _id

    def run(self):
        return 0

    def toString(self):
        return str(self.INSTRUCTION_ID)
