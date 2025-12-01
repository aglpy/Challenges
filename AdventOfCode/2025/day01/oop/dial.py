""" Dial to open the entrance """

class Dial:
    """ Dial to open the entrance """
    position: int
    positions: int = 100

    def __init__(self, start_position: int):
        self.position = start_position

    def turn_right(self):
        """ Turn right """
        self.position = (self.position + 1) % self.positions
    
    def turn_left(self):
        """ Turn left """
        self.position = (self.position - 1) % self.positions
