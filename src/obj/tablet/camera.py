import pygame

from obj.element import Element


class Camera(Element):

    def __init__(self, position: tuple[int, int], window: pygame.Surface, image: pygame.Surface):
        self.image = image
        image_rect = self.image.get_rect()
        super().__init__(image_rect, window)

        # Set position of image (otherwise it's (0, 0))
        self.x = position[0]
        self.y = position[1]
        
       
    def update(self):
        self.window.blit(self.image, (self.x, self.y))