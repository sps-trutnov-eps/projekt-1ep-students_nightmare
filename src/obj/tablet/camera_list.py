import pygame

from obj.element import Element
from obj.tablet.camera import Camera


class CameraList(Element):

    def __init__(self, tablet, window: pygame.Surface) -> None:
        rect = pygame.Rect(tablet.x, tablet.y, 300, 40)
        super().__init__(rect, window)
        self.camera_count = 5
        self.list: list[Camera] = []
        self.surface = pygame.Surface((self.width, self.height))
        
        i = 0
        while i > self.camera_count:
            image = pygame.image.load('visuals/levedverezavrene.png')
            camera = Camera((tablet.x, tablet.y), self.window, "Name", image)
            print(camera.image)
            self.list.append(camera)
            i += 1

        for camera in self.list:
            self.surface.blit(camera.image)