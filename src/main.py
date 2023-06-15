import pygame

from obj.tablet.tablet import Tablet
from obj.tablet.camera import Camera
from obj.tablet.tablet_button import TabletButton
from obj.computer.computer import Computer
from obj.doors.doors import Doors

pygame.init()

# Game window's variables
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tablet = Tablet(window)
tablet_button = TabletButton(window)
computer = Computer()
doors = Doors((50, 50, 50, 50),(100, 200, 50),(100, 300, 100, 300))
doors_right = Doors((1820, 50, 50, 50),(100, 200, 50),(1720, 300, 100, 300))

while True:
    # Events
    for event in pygame.event.get():
        # Easily exit the game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    
    doors.sance_nastavit_ucitele()
    doors.odpocet_jumpscare(window)
    doors.kontrola_stisku_tlacitka()
    doors.vykreslit(window)
    
    doors_right.sance_nastavit_ucitele()
    doors_right.odpocet_jumpscare(window)
    doors_right.kontrola_stisku_tlacitka()
    doors_right.vykreslit(window)
    
    pygame.display.update()