import configparser
import pygame
from obj.element import Element

window = configparser.ConfigParser()
window.read("data/window.ini")

elements = configparser.ConfigParser()
elements.read("data/elements.ini")


class Doors(Element):

    def __init__(self) -> None:
        pos_y = (window.getint("Dimensions", "HEIGHT") // 2)
        pos_x = (window.getint("Dimensions", "WIDTH") // 2)
        super().__init__((pos_x,pos_y),
                         (elements.getint("Doors", "WIDTH"), elements.getint("Doors", "HEIGHT"))) 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
    def toggle(self):
        self.showed = True
        
    def get_pressed(self, window, mouse):
        pass
    
    def render(self, window: pygame.surface):
        self.window = window
        pygame.draw.rect(window, (155,155,155), self.rect)
        

            
            