import pygame
import random
from obj.computer.computer import Computer
from obj.doors.doors import Doors
from obj.tablet.tablet_krejdl import Tablet
pygame.init()
jake_dvere = 0
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
        if tablet.neni_u_kamer() and jake_dvere == 0:
            jake_dvere = random.randint(1,2)

            if jake_dvere == 1:
                doors.nastavit_ucitele()
            if jake_dvere == 2:
                doors_right.nastavit_ucitele()
        if not doors.ucitel_u_dveri and not doors_right.ucitel_u_dveri and tablet.neni_u_kamer():
            jake_dvere = 0
            tablet.je_zpatky_u_kamer()
            
        
        doors.kontrola_stisku_tlacitka()
        doors_right.kontrola_stisku_tlacitka()
        
        if tablet.pozice_ucitele == [False, False, False, False] and not doors.ucitel_u_dveri and not doors_right.ucitel_u_dveri:
            tablet.pozice_ucitele = [True, False, False, False]
                
        doors.vykreslit(window)
        doors_right.vykreslit(window)

        tablet.posunout()
        tablet.vykreslit(window)
        
        doors.odpocet_jumpscare(window)
        doors_right.odpocet_jumpscare(window)
        
        
    pygame.display.update()
