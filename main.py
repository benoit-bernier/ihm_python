#!/usr/bin/python3
# -*- coding: utf-8 -*-

from p5 import *
import pyfirmata

from piou_p5 import *
from jeu import *
from terrain_p5 import Terrain_p5
import util

piou = None
terrain = None 
jeu = None

micro_pin=None 
bouton_pin=None 
buzzer_pin=None 
it=None 
board = None

f=None

def setup():
    """
        Initialise toute l'installation avec arduino et les modules
        ...
                    
        Auteur Benoit
        """
    global piou, terrain, jeu,  micro_pin, bouton_pin, buzzer_pin, it, board, f

    f = create_font("arial.ttf", 32)

    size(util.SCREEN_X, util.SCREEN_Y)

    piou = Piou_P5(int(util.SCREEN_Y // 2))
    terrain = Terrain_p5()
    jeu = Jeu(terrain, piou)

    board = pyfirmata.Arduino(util.PORT)
    print("communication successfully started")

    micro_pin = board.digital[util.MICRO]
    bouton_pin = board.digital[util.BOUTON]
    buzzer_pin = board.digital[util.BUZZER]

    micro_pin.mode = pyfirmata.INPUT
    micro_pin.enable_reporting()

    bouton_pin.mode = pyfirmata.INPUT
    bouton_pin.enable_reporting()

    buzzer_pin.mode = pyfirmata.OUTPUT

    it = pyfirmata.util.Iterator(board)
    it.start()

def draw():
     """
        Initialise P5
        ...
        auteur : Benoit
    """

    global piou, terrain, jeu, micro_pin, bouton_pin, buzzer_pin, it, board, f
    if jeu.arret_jeu :
        background(0)
        text_align("CENTER", "CENTER")
        text_font(f)
        fill(255)
        text("Vous avez terminé le jeu", util.SCREEN_X//2, util.SCREEN_Y//2-20)
        text("Votre score est de {}".format(jeu.score), util.SCREEN_X//2, util.SCREEN_Y//2+20)
    else:
        terrain.avancer(jeu.vitesse)
        if not bouton_pin.read():
            piou.bouger_de(-5)
            it = pyfirmata.util.Iterator(board)
            it.start()
        elif (key_is_pressed and key in util.LISTE_BAS) or (micro_pin.read()):
            piou.bouger_de(5)
            it = pyfirmata.util.Iterator(board)
            it.start()

        if terrain.intersect(piou):
            print("Le jeu s'arrête là, tu as obtenu un score de {}".format(jeu.score))
            jeu.arreter_jeu()
            buzzer_pin.write(1)
        else:
            jeu.score += 1

        terrain.display()
        piou.display()

if __name__ == '__main__':
    run()
