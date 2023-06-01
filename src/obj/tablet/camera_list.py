import pygame

from obj.element import Element
from obj.tablet.camera import Camera


class CameraList(Element):

    def __init__(self, tablet, parent_surface: pygame.Surface) -> None:
        super().__init__((400, 80), (20, 20), parent_surface)
        self.camera_count = 5
        self.list: list[Camera] = []
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        
        i = 0
        while i < self.camera_count:
            image = pygame.Surface((55, 55))
            image.fill((255,0,0))
            camera = Camera((tablet.x, tablet.y), self.surface, "Name", image)
            self.list.append(camera)
            self.surface.blit(camera.image, (40*i + 40*i, 0))
            i += 1