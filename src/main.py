import pygame

from obj.tablet.tablet import Tablet
from obj.computer.computer import Computer
from obj.doors.doors import Doors


pygame.init()

# Game window's variables
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tablet = Tablet()
computer = Computer()
doors = Doors()


while True:

    # Events
    for event in pygame.event.get():
        # Easily exit the game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    tablet.update(window)
    doors.render(window)

    pygame.display.update()