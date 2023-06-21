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
        super().__init__((elements.getint('Tablet', 'WIDTH'), elements.getint('Tablet', 'HEIGHT')), (pos_x, pos_y), window)
        self.showed = True
        self.camera_list = CameraList(self, window)
        self.surface.fill((255,255,255))
    
    def toggle(self) -> bool:
        if self.showed:
            self.showed = False
        else:
            self.showed = True
        return self.showed
    
    def printCameraList(self):
        self.surface.blit(self.camera_list.surface, (20, 20))

    def update(self) -> None:
        if self.showed:
            self.target_surface.blit(self.surface, (self.x, self.y))