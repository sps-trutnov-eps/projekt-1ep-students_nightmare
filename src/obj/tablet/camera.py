import pygame

from obj.element import Element


class Camera(Element):

    def __init__(self, position: tuple[int, int], parent_surface: pygame.Surface, name: str, image: pygame.Surface = None):
        if image != None:
            self.image = image
        self.name = name
        super().__init__((55,55), position, parent_surface)

        # Set position of image (otherwise it's (0, 0))
        self.x = position[0]
        self.y = position[1]