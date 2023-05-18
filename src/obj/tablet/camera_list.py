import pygame

from obj.element import Element
from obj.tablet.tablet import Tablet


class CameraList(Element):

    def __init__(self, tablet: Tablet, window: pygame.Surface) -> None:
        rect = pygame.Rect(tablet.x, tablet.y, 300, 40)
        super().__init__(rect, window)