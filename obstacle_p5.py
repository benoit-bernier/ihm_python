from p5 import *

import util
from obstacle import Obstacle

class Obstacle_P5 (Obstacle):
    """
    Classe représentant un obstacle p5, hérite de la classe Obstacle
    ...
    Attributs
    -----
    min_y : int
        Position en y
    pos_x : int
        Position en x
    largeur : int
        largeur de l'obstacle
    hauteur : int
        hauteur de l'obstacle
    couleur : Color
        Couleur de l'obstacle

    Méthodes
    -----
    avancer(v):
        Retranche v à la position en x de l'obstacle
    afficher():
        Affiche l'obstacle en chaîne de caractères dans la console  
    display()
        Affiche l'obstacle dans p5

    auteur : Benoît
    """
    def __init__(self, min_y, pos_x, largeur=util.LARGEUR_OBSTACLE, hauteur=util.HAUTEUR_CHEMIN, couleur=util.COULEUR):
        """
        Initialise l'objet obstacle_p5
        ...
        Attributs
        -----
        min_y : int
            Position en y
        pos_x : int
            Position en x
        largeur : int
            largeur de l'obstacle
        hauteur : int
            hauteur de l'obstacle
        couleur : Color
            Couleur de l'obstacle
        """
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