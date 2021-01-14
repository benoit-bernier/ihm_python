from p5 import *

from piou import Piou

class Piou_P5 (Piou):
    def display(self):
        fill(Color(218, 247, 166))
        circle(self.pos_x, self.pos_y, self.radius)