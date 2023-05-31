import pygame
import configparser

from obj.element import Element
from obj.tablet.camera_list import CameraList


window_config = configparser.ConfigParser()
window_config.read('data/window.ini')

elements = configparser.ConfigParser()
elements.read('data/elements.ini')


class Tablet(Element):
    
    def __init__(self, window: pygame.Surface) -> None:
        pos_x = window_config.getint('Dimensions', 'WIDTH') / 2 - elements.getint('Tablet', 'WIDTH') / 2
        pos_y = window_config.getint('Dimensions', 'HEIGHT') / 2 - elements.getint('Tablet', 'HEIGHT') / 2
        super().__init__(pygame.Rect(pos_x, pos_y, elements.getint('Tablet', 'WIDTH'), elements.getint('Tablet', 'HEIGHT')), window)
        self.showed = True
        self.camera_list = CameraList(self, self.window)
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255,255,255))
    
    
    def toggle(self) -> bool:
        if self.showed:
            self.showed = False
        else:
            self.showed = True
        return self.showed
    
    def printCameraList(self):
        self.surface.blit(self.camera_list.surface, (self.x, self.y))

    def update(self) -> None:
        if self.showed:
            pygame.draw.rect(self.surface, (255,255,255), self.rect)
            self.window.blit(self.surface, (self.x, self.y))