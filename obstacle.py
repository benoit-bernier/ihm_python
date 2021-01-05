from p5 import *
import util

class Obstacle:
    def __init__(self, min_y, pos_x, largeur=util.LARGEUR_OBSTACLE, hauteur=util.HAUTEUR_CHEMIN, couleur=util.COULEUR):
        """
        Initialise un objet Obstacle, défini par sa position minimale en y (début du chemin), et sa position en x. 
            Les propriétés largeur et hauteur sont initialisées avec les valeurs constantes d'util.
        """
        self.min_y = min_y
        self.pos_x = pos_x
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur

    def avancer(self, v):
        """
        Retranche v à la position en x de l'obstacle
        """
        self.pos_x -= v
    
    def afficher(self):
        """
        Affiche l'obstacle en chaîne de caractères dans la console
        """
        print("   L'obstacle est en x={}, y={}".format(self.pos_x, self.min_y))
    
    def display(self):
        """
        Affiche l'obstacle dans p5
        """
        print("################################################TOP")
        stroke(51)
        fill(self.couleur)
        rect((self.pos_x, 0, self.largeur, self.min_y))
        rect((self.pos_x, self.min_y + self.hauteur, self.largeur, util.SCREEN_Y-(self.min_y + self.hauteur)))