import pygame


class Element:

    def __init__(self, rect: pygame.Rect, position: tuple[int]) -> None:
        self.rect = rect
        self.x: int = position[0]
        self.y: int = position[1]
        self.width: int = rect.width
        self.height: int = rect.height
        

    def clicked() -> bool:
        pass