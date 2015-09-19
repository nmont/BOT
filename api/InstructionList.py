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
            if instruction == api.LEFT_BUMPER_END and not self.left_bumper.on_left:
                self.on_left = False
            else:
                self.left_bumper.append_instruction(instruction)
                return 1
        elif self.on_right:
            if self.right_bumper is None:
                self.right_bumper = InstructionList()
            if instruction == api.RIGHT_BUMPER_END and not self.right_bumper.on_right:
                self.on_right = False
            else:
                self.right_bumper.append_instruction(instruction)
                return 2
        # TODO - FIGURE OUT HOW TO TELL WHEN THE NEXT LEVEL DOWN IS FINISHED WITH BUMPER BLOCK
        elif instruction == api.LEFT_BUMPER_START:
            self.on_left = True
        elif instruction == api.RIGHT_BUMPER_START:
            self.on_right = True
        else:
            self.main_list.append(instruction)
            return 0
