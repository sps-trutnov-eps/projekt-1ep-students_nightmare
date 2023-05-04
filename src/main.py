import pygame

from obj.tablet.tablet import Tablet
from obj.tablet.tablet_button import TabletButton
from obj.computer.computer import Computer
from obj.doors.doors import Doors

pygame.init()

# Game Window's variables
screen_width = 1920
screen_height = 1080

# Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

tablet = Tablet()
tablet_button = TabletButton()
computer = Computer()
doors = Doors()


while True:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
               
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE  :
            exit()