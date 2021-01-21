from p5 import *

from terrain import Terrain

class Terrain_p5 (Terrain):
    def display(self):
        """
        Affiche le terrain dans p5
        """
        background(250)
        for i in range(len(self.obstacles)):
            self.obstacles[i].display()
            