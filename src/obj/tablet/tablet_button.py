import pygame
from obj.element import Element

class TabletButton:
    
    def __init__(self):
        self.image = pygame.image.load("obj/tablet/Visuals/tabletbutton.png")
        self.rect = self.image.get_rect()

    def update(self):
        pass


            


