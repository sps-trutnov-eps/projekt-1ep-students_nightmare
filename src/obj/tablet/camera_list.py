import pygame
import configparser

from obj.element import Element
from obj.tablet.camera import Camera


teachers_config = configparser.ConfigParser()
teachers_config.read('data/teachers.ini')
teacher_list = teachers_config.get('Teachers', 'teacher_list')
teachers = teacher_list.split(',')


class CameraList(Element):

    def __init__(self, tablet, parent_surface: pygame.Surface) -> None:
        super().__init__((400, 80), (20, 20), parent_surface)
        self.list: list[Camera] = []
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))

        i = 0
        for teacher_name in teachers:
            image = pygame.Surface((55, 55))
            image.fill((255,0,0))
            camera = Camera((tablet.x, tablet.y), self.surface, teacher_name, image)
            self.list.append(camera)
            self.surface.blit(camera.image, (40*i + 40*i, 0))
            i += 1