import random
from p5 import *

#~~~~~~ CONSTANTES ~~~~~~
SCREEN_X = 900
SCREEN_Y = 600
LARGEUR_OBSTACLE = 100
HAUTEUR_CHEMIN = 100
POS_X_PIOU = 250
FACTEUR_DECALAGE_Y = 10
COULEUR = Color(125, 255, 125)

def calcul_nouvelle_pos_y(pos_y_prec):
    sens = 1 if random.randint(0,1) else -1
    difference = random.randint(0, (SCREEN_X/HAUTEUR_CHEMIN) * FACTEUR_DECALAGE_Y)
    return pos_y_prec + (sens * difference)

