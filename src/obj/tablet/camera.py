import pygame
from obj.element import Element


class Camera(Element):

    def __init__(self, image: pygame.Surface, window: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect()
        x = window.get_width() / 2 - self.rect.width / 2
        y = window.get_height() - self.rect.height
        super().__init__((x, y), (self.rect.width, self.rect.height))
                
        self.window = window

       
    def update(self):

        self.window.blit(self.image, (self.x, self.y))
