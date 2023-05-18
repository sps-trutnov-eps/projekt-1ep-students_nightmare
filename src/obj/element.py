import pygame


class Element:

    def __init__(self, rect: pygame.Rect) -> None:
        self.rect: pygame.Rect = rect
        self.x: int = rect.x
        self.y: int = rect.y
        self.width: int = rect.width
        self.height: int = rect.height
        

    def touched(self, mouse: pygame.mouse) -> bool:
        return self.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1])
    
    def clicked(self, mouse: pygame.mouse) -> bool:
        if mouse.get_pressed()[0]:
            return self.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1])
        return False