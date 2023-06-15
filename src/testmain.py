from discord import Discord #
import pygame as pg
import sys
import random as rm #

random_counter = 60 #
random_cislo = 0 #

clock = pg.time.Clock()
fps = 60

obraz = pg.display.set_mode((1280, 720))

dc = Discord(200, 100, 100, 100, obraz, 300) #

while True:
    obraz.fill((0, 255, 255))

    keys = pg.key.get_pressed()
    events = pg.event.get()
    mousepos = pg.mouse.get_pos()
    mousepress = pg.mouse.get_pressed(num_buttons=3)

    for i in events:
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if keys[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()

    if random_counter >= 10: #
        random_cislo = rm.randrange(1, 150) #
        random_counter = 0 #

    random_counter += 1 #

    smrt = dc.detect(mousepos, mousepress) #
    if smrt == True: # ??
        pg.quit()
        sys.exit()
    dc.event(random_cislo) #
    dc.show() #

    clock.tick(fps)
    pg.display.update()