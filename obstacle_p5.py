from p5 import *

import util
from obstacle import Obstacle

class Obstacle_P5 (Obstacle):
    
    def __init__(self, min_y, pos_x, largeur=util.LARGEUR_OBSTACLE, hauteur=util.HAUTEUR_CHEMIN, couleur=util.COULEUR):
        super().__init__(min_y, pos_x)
        self.couleur = couleur

    def display(self):
        """
        Affiche l'obstacle dans p5
        """
        stroke(51)
        fill(self.couleur)
        rect(self.pos_x, 0, self.largeur, self.min_y)
        rect(self.pos_x, self.min_y + self.hauteur, self.largeur, util.SCREEN_Y-(self.min_y + self.hauteur))