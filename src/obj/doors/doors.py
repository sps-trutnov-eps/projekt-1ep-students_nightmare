import configparser
import pygame
from obj.element import Element
window = configparser.ConfigParser()
window.read("data/window.ini")

elements = configparser.ConfigParser()
elements.read("data/elements.ini")


class Doors(Element):

    def __init__(self) -> None:
        pos_y = 700
        pos_x = 500
        super().__init__((pos_x,pos_y),
                         (window.getint("dimensions", "width"), window.getint("dimensions", "height"))) 
        self.rect = pygame.rect(self.x, self.y, self.width, self.height)
        
        
    def toggle(self):
        self.showed = True
            
        

    def render(self, window: pygame.surface):
        pygame.draw.rect(window, (155,155,155), self.rect)
            