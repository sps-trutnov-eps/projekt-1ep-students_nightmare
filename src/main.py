import pygame

from obj.tablet.tablet import Tablet
from obj.computer.computer import Computer
from obj.doors.doors import Doors


pygame.init()

# Game window's variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Game window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tablet = Tablet()
computer = Computer()
door1 = Doors((50,50,50,50), (0,255,0), (100,300,100,300))




while True:
    # Events
    for event in pygame.event.get():
        # Easily exit the game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    
    door1.sance_nastavit_ucitele()
    door1.odpocet_jumpscare()
    door1.kontrola_stisku_tlacitka()
    door1.vykreslit(window)
    
    pygame.display.update()