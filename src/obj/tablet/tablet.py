import pygame
import configparser

from obj.element import Element


window = configparser.ConfigParser()
window.read('data/window.ini')

elements = configparser.ConfigParser()
elements.read('data/elements.ini')


class Tablet(Element):
    
    def __init__(self) -> None:
        pos_x = window.getint('Dimensions', 'WIDTH') / 2 - elements.getint('Tablet', 'WIDTH') / 2
        pos_y = window.getint('Dimensions', 'HEIGHT') / 2 - elements.getint('Tablet', 'HEIGHT') / 2
        super().__init__(pygame.Rect(pos_x, pos_y, elements.getint('Tablet', 'WIDTH'), elements.getint('Tablet', 'HEIGHT')))
        self.showed = False
    
    
    def toggle(self) -> bool:
        if self.showed:
            self.showed = False
        else:
            self.showed = True
        return self.showed

    def update(self, window: pygame.Surface) -> None:
        if self.showed:
            pygame.draw.rect(window, (255,255,255), self.rect)