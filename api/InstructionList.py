__author__ = 'Ben Williams'

import api


class InstructionList:

    def __init__(self):
        self.main_list = []
        self.left_bumper = None
        self.right_bumper = None
        self.on_right = False
        self.on_left = False

    def append_instruction(self, instruction):
        if self.on_left:
            if self.left_bumper is None:
                self.left_bumper = InstructionList()
            self.left_bumper.append_instruction(instruction)
            return 1
        elif self.on_right:
            if self.right_bumper is None:
                self.right_bumper = InstructionList()
            self.right_bumper.append_instruction(instruction)
            return 2
        # TODO - FIGURE OUT HOW TO TELL WHEN THE NEXT LEVEL DOWN IS FINISHED WITH BUMPER BLOCK
        elif instruction == api.LEFT_BUMPER_START:
            self.on_left = True
        elif instruction == api.LEFT_BUMPER_END:
            self.on_left = False
        elif instruction == api.RIGHT_BUMPER_START:
            self.on_right = True
        elif instruction == api.RIGHT_BUMPER_END:
            self.on_right = False
        else:
            self.main_list.append(instruction)
            return 0