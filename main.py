from p5 import *

from piou import *
from jeu import *
from terrain import Terrain
import util

piou = None
terrain = None
jeu = None

f = None

def setup():
    global piou, terrain, jeu
    size(util.SCREEN_X, util.SCREEN_Y)

    piou = Piou(int(util.SCREEN_Y // 2))
    terrain = Terrain()
    jeu = Jeu(terrain, piou)

def draw():
    global piou, terrain, jeu
    if jeu.arret_jeu :
        background(0)
        text_align("CENTER", "CENTER")
        text("Vous avez terminé le jeu", util.SCREEN_X//2, util.SCREEN_Y//2)
    else:
        terrain.avancer(jeu.vitesse)
        if key_is_pressed and key in util.LISTE_HAUT:
            piou.bouger_de(-5)
        elif key_is_pressed and key in util.LISTE_BAS:
            piou.bouger_de(5)

        if False: #terrain.intersect(piou):
            print("Le jeu s'arrête là, tu as obtenu un score de {}".format(jeu.score))
            jeu.arreter_jeu()
        else:
            jeu.score += 1

        terrain.display()
        piou.display()

if __name__ == '__main__':
    run()
