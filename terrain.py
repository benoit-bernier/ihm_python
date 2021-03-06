import util
from collections import deque

from obstacle_p5 import *

class Terrain:
    """
    Classe représentant un terrain
    ...
    Attributs
    -----
    obstacles :
        Liste des obstacles composant le terrain
    
    Méthodes
    -----
    nouvel_obstacle():
        Ajoute un obstacle à la file d'obstacles de l'objet
    init_obstacles():
        Initialise la file d'obstacle
    intersect(piou):
        Retourne un booleen indiquant si le piou possède une intersection avec l'un des obstacles
    avancer(vitesse):
        Fait avancer tous les obstacles du terrain de n où n=vitesse
    afficher():
        Affiche le terrain en chaîne de caractères dans la console

    auteur : Benoît
    """
    def __init__(self, obstacles=deque()):
        """
        Initialise un objet Terrain avec une nouvelle file d'obstacles
        
        Parametres
        -----
        obstacles : Deque, optionnel
            Queue d'obstacles, vide par défaut
        """
        self.obstacles=obstacles
        self.init_obstacles()

    def nouvel_obstacle(self):
        """
        Ajoute un obstacle à la file d'obstacles de l'objet
        """        
        self.obstacles.append(
            Obstacle_P5(
                util.calcul_nouvelle_pos_y(self.obstacles[-1].min_y),
                self.obstacles[-1].pos_x+util.LARGEUR_OBSTACLE,
                couleur=util.random_color()
            )
        )     

    def init_obstacles(self):
        """
        Initialise la file d'obstacle
        """
        self.obstacles=deque()  
        self.obstacles.append(
            Obstacle_P5(
                int((util.SCREEN_Y/2)-(util.HAUTEUR_CHEMIN/2)), #Centre le chemin sur la hauteur de l'écran
                0
            )
        )
        for _ in range(int(util.SCREEN_X//util.LARGEUR_OBSTACLE)): 
            self.nouvel_obstacle()

    def intersect(self, piou):
        """
        Retourne un booleen indiquant si le piou possède une intersection avec l'un des obstacles
        ...
        Parametres
        ----------
        piou: Piou
            le piou sur lequel on regarde s'il y a intersection avec les obstacles

        Returns
        -------
        bool
            Le terrain et le piou présentent une intersection
        """
        pos_piou=int(piou.pos_x//util.LARGEUR_OBSTACLE)
        #Pas besoin d'autant de variable, mais ça simplifie la lecture
        obstacle1=self.obstacles[pos_piou]
        obstacle2=self.obstacles[pos_piou + 1]

        depend_obs1 = obstacle1.pos_x < piou.pos_x < (obstacle1.pos_x + util.HAUTEUR_CHEMIN)
        tape_obs2 = (piou.pos_y < obstacle1.min_y) or (piou.pos_y > (obstacle1.min_y + util.HAUTEUR_CHEMIN))

        depend_obs2 = obstacle2.pos_x < piou.pos_x < (obstacle2.pos_x + util.HAUTEUR_CHEMIN)
        tape_obs1 = (piou.pos_y < obstacle2.min_y) or (piou.pos_y > (obstacle2.min_y + util.HAUTEUR_CHEMIN))

        intersect_obstacle1 =  depend_obs1 and tape_obs1
        intersect_obstacle2 = depend_obs2 and tape_obs2

        return intersect_obstacle1 or intersect_obstacle2

    def avancer(self, vitesse):
        """
        Fait avancer tous les obstacles du terrain de n où n=vitesse
        ...
        Parameters
        ----------
        vitesse: int
            l'entier naturel dont on va retrancher la position en x de chacun des obstacles
        """
        for i in self.obstacles:
            i.avancer(vitesse)
        
        if(self.obstacles[0].pos_x <= -1*util.LARGEUR_OBSTACLE): #On regarde si l'élément de gauche n'est plus visible
            self.obstacles.popleft() #Bizarrement le pop par défaut défile à droite, comportement d'une stack
            self.nouvel_obstacle()

    def afficher(self):
        """
        Affiche le terrain en chaîne de caractères dans la console
        """
        print("Le terrain est composé de {} obstacles : ".format(len(self.obstacles)))
        for i in range(len(self.obstacles)):
            self.obstacles[i].afficher()
        print("   Fin du dernier obstacle : {}".format(self.obstacles[-1].pos_x + util.LARGEUR_OBSTACLE))

