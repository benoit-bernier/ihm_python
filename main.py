from p5 import *
import pyfirmata

from piou_p5 import *
from jeu import *
from terrain_p5 import Terrain_p5
import util

piou = None
terrain = None
jeu = None

f = None

micro_pin = None
it=None
board=None

def setup():
    global piou, terrain, jeu, micro_pin, it, board
    size(util.SCREEN_X, util.SCREEN_Y)

    piou = Piou_P5(int(util.SCREEN_Y // 2))
    terrain = Terrain_p5()
    jeu = Jeu(terrain, piou)

    board = pyfirmata.Arduino("/dev/ttyACM0")
    print("communication successfully started")

    micro_pin = board.digital[3]
    micro_pin.mode = pyfirmata.INPUT
    micro_pin.enable_reporting()
    it = pyfirmata.util.Iterator(board)
    it.start()

def draw():
    global piou, terrain, jeu, micro_pin, it, board
    if jeu.arret_jeu :
        background(0)
        text_align("CENTER", "CENTER")
        text("Vous avez terminé le jeu", util.SCREEN_X//2, util.SCREEN_Y//2)
    else:
        terrain.avancer(jeu.vitesse)
        if not micro_pin.read():
            piou.bouger_de(-5)
            it = pyfirmata.util.Iterator(board)
            it.start()
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
