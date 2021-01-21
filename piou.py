import util

class Piou:
    def __init__(self, pos_y, pos_x=util.POS_X_PIOU, radius=util.radius_PIOU):
        """
        Initialise l'objet Piou à une position en y pos_y. 
            La propriété pos_x est définie à partir d'une constante d'util.
        """
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.radius = radius


    def set_pos_y(self, i):
        """
        Modifie la propriété pos_y à i
        """
        # TODO: à l'avenir contrôler i et le modifier ou lever une exception.
        self.pos_y = i
    
    def bouger_de(self, i):
        """
        Modifie la propriété pos_y de i
        ...
        Parameters
        ----------
        i: Int
            Le nombre de pixels de décalage du piou sur l'axe y. Négatif pour remonter, positif pour descendre
        """
        if self.pos_y - self.radius <= 0:
            self.pos_y = 0 + self.radius
        elif self.pos_y + self.radius >= util.SCREEN_Y:
            self.pos_y = util.SCREEN_Y - self.radius
        else :
            self.pos_y += i