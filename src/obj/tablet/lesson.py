import pygame


class Lesson:

    def __init__(self, name: str, image: pygame.Surface) -> None:
        self.name = name
        self.image = image