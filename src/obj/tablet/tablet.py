import  pygame
import sys


class Tablet:
    
    def __init__(self, position_x, position_y, image):
        self.showed = False
        self.x = position_x
        self.y = position_y
        self.image = image
    
    
    def toggle(self):
        # add or remove showing tablet
        self.showed= not self.showed
        
        