import pygame

from obj.tablet.tablet import Tablet
from obj.tablet.camera import Camera
from obj.tablet.tablet_button import TabletButton
from obj.computer.computer import Computer
from obj.doors.doors import Dvere as Doors

pygame.init()

# Game window's variables
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tablet = Tablet(window)
tablet_button = TabletButton(window)
computer = Computer()
doors = Doors(pygame.mouse.get_pos(), (30, 30), (255,255,255), (50, 150))


while True:

    # Events
    for event in pygame.event.get():
        # Easily exit the game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    

    window.fill((0,0,0))

    if tablet_button.clicked(pygame.mouse):
        tablet.toggle()
    tablet.printCameraList()
    tablet.update()
    tablet_button.update()

    
    pygame.display.update()