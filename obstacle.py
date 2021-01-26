import util

class Obstacle:
    """
    Classe représentant un obstacle
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

    Méthodes
    -----
    avancer(v):
        Retranche v à la position en x de l'obstacle
    afficher():
        Affiche l'obstacle en chaîne de caractères dans la console  

    auteur : Benoît
    """
    def __init__(self, min_y, pos_x, largeur=util.LARGEUR_OBSTACLE, hauteur=util.HAUTEUR_CHEMIN):
        """
        Initialise un objet Obstacle, défini par sa position minimale en y (début du chemin), et sa position en x. 
            Les propriétés largeur et hauteur sont initialisées avec les valeurs constantes d'util.
        ...
        Parametres :
        -----
        min_y : int
            Position en y
        pos_x : int
            Position en x
        largeur : int
            largeur de l'obstacle
        hauteur : int
            hauteur de l'obstacle
        """
        self.min_y = min_y
        self.pos_x = pos_x
        self.largeur = largeur
        self.hauteur = hauteur

    def avancer(self, v):
        """
        Retranche v à la position en x de l'obstacle
        ...
        Parametres
        -----
        v : int
            vitesse de déplacement
        """
        self.pos_x -= v
    
    def afficher(self):
        """
        Affiche l'obstacle en chaîne de caractères dans la console
        """
        print("   L'obstacle est en x={}, y={}".format(self.pos_x, self.min_y))