import pygame

class Camera(pygame.sprite.Sprite):
    def __init__(self,x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
       
    def update(self):
        # Destroying the pipe
        self.rect.x -= self.pipe_speed
        if self.rect.x <= -200: 
            self.kill()

    def destroy(self):
        self.kill() 