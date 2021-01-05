from p5 import *

from piou import *
from jeu import *
from terrain import Terrain
import util

piou = None
terrain = None
jeu = None


def setup():
    global piou, terrain, jeu
    size(util.SCREEN_X, util.SCREEN_Y)

    piou = Piou(int(util.SCREEN_Y // 2))
    terrain = Terrain()
    jeu = Jeu(terrain, piou, vitesse=1)


def draw():
    global piou, terrain, jeu

    terrain.afficher()
    terrain.display()
    piou.afficher()
    piou.display()
    terrain.avancer(jeu.vitesse)
    piou.set_pos_y(util.calcul_nouvelle_pos_y(300))
    if terrain.intersect(piou):
        print("Le jeu s'arrête là, tu as obtenu un score de {}".format(jeu.score))
        jeu.arreter_jeu()
    else:
        jeu.score += 1

if __name__ == '__main__':
    run()
