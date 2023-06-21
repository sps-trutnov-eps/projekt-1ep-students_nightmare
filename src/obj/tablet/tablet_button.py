import pygame
from obj.element import Element

class TabletButton(Element):
    
    def __init__(self, window: pygame.Surface):


        self.image = pygame.image.load("obj/tablet/tabletbutton.png")
        self.rect = self.image.get_rect()
        x = window.get_width() / 2 - self.rect.width / 2
        y = window.get_height() - self.rect.height
        super().__init__((self.rect.width, self.rect.height), (x, y), window)
        
        self.surface.blit(self.image, (0, 0))