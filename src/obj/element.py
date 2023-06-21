import pygame


class Element:

    def __init__(self, dimensions: tuple[int, int], position: tuple[int, int], parent_surface: pygame.Surface) -> None:
        self.target_surface = parent_surface
        self.surface = pygame.Surface((dimensions[0], dimensions[1]))
        self.rect: pygame.Rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
        self.x: int = self.rect.x
        self.y: int = self.rect.y
        self.width: int = self.rect.width
        self.height: int = self.rect.height
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
        self.target_surface.blit(self.surface, (self.x, self.y))