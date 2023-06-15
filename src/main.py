import pygame
from discord import Discord #
import random as rm #
import pygame as pg

# Discord
random_counter = 60 #
random_cislo = 0 #
clock = pg.time.Clock()
fps = 60

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
doors = Doors()
dc = Discord(400, 250, 500, 500, window) #

while True:

    # Events
    for event in pygame.event.get():
        # Easily exit the game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    window.fill((0,0,0))

    # Discord
    keys = pg.key.get_pressed() #

    if random_counter >= 10: #
        random_cislo = rm.randrange(1, 150) #
        random_counter = 0 #

    random_counter += 1 #

    dc.detect(keys) #
    dc.event(random_cislo) #
    dc.show() #

    if tablet_button.clicked(pygame.mouse):
        tablet.toggle()
    tablet.printCameraList()
    tablet.update()
    tablet_button.update()

    clock.tick(fps)
    pygame.display.update()