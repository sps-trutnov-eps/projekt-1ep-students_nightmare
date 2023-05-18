import pygame


class Element:

    def __init__(self, rect: pygame.Rect, window: pygame.Surface) -> None:
        self.window = window
        self.rect: pygame.Rect = rect
        self.x: int = rect.x
        self.y: int = rect.y
        self.width: int = rect.width
        self.height: int = rect.height
        self.last_clicked = 0
        

    def touched(self, mouse: pygame.mouse) -> bool:
        return self.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1])
    
    def clicked(self, mouse: pygame.mouse) -> bool:
        time = pygame.time.get_ticks()
        if time > self.last_clicked + 100:
            self.last_clicked = time
            if mouse.get_pressed()[0]:
                return self.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1])
            return False
        
    def update(self) -> None:
        pygame.draw.rect(self.window, (255,255,255), self.rect)