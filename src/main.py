import pygame

from obj.computer.computer import Computer
from obj.doors.doors import Doors
from obj.tablet.tablet_krejdl import Tablet
pygame.init()

# Game window's variables
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


computer = Computer()
doors = Doors((50, 50, 50, 50),(100, 200, 50),(100, 300, 100, 300))
doors_right = Doors((1820, 50, 50, 50),(100, 200, 50),(1720, 300, 100, 300))
tablet = Tablet()

while True:
    # Events
    for event in pygame.event.get():
        # Easily exit the game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
            
            
    if not doors.game_over_happened:
        doors.sance_nastavit_ucitele()
        doors.kontrola_stisku_tlacitka()
        doors_right.sance_nastavit_ucitele()
        doors_right.kontrola_stisku_tlacitka()
        
        doors.vykreslit(window)
        doors_right.vykreslit(window)

        doors.odpocet_jumpscare(window)
        doors_right.odpocet_jumpscare(window)
        tablet.vykreslit(window)
        
        
    pygame.display.update()
