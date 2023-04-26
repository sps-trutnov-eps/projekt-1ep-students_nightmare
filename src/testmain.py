from discord import Discord
import pygame as pg
import sys
import random as rm

obraz = pg.display.set_mode((1280, 720))

dc = Discord(200, 100, 100, 100, obraz)

while True:
    obraz.fill((255, 255, 255))

    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()

    random_cislo = rm.randrange(1, 10000)

    dc.event(random_cislo)
    dc.show()

    pg.display.update()