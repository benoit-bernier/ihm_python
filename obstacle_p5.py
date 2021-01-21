from p5 import *

import util
from obstacle import Obstacle

class Obstacle_P5 (Obstacle):
    def display(self):
        """
        Affiche l'obstacle dans p5
        """
        stroke(51)
        fill(self.couleur)
        rect(self.pos_x, 0, self.largeur, self.min_y)
        rect(self.pos_x, self.min_y + self.hauteur, self.largeur, util.SCREEN_Y-(self.min_y + self.hauteur))