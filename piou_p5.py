from p5 import *

from piou import Piou

class Piou_P5 (Piou):
    """
    Dessine le personnage du jeu sous la forme d'un petit moineau
    
    auteur : adam
    """
    def display(self):
        #fill(Color(218, 247, 166))
        #circle(self.pos_x, self.pos_y, self.radius)
        with push_matrix():
            translate(self.pos_x, self.pos_y)
            scale(0.3)
            fill(0)
            ellipse(50,20, 40, 40)
            rect(45,15,25,20)
            triangle(70,18,70,35,80,25)
            arc((50, 35), 40, 80, 0, PI + QUARTER_PI, mode="PIE")
            triangle(50,75,0,75,45,2)
            fill(255)
            ellipse(55,15,5,5)
            fill(0)