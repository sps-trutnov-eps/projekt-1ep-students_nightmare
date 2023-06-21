import random
import pygame
import time
from obj.doors.doors import Dvere
pygame.init()
mys = pygame.mouse.get_pos()
okno = pygame.display.set_mode((800,800))
doors = Dvere(mys, (400,300,50,50), (0,255,0), (400,300,50,50))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
    

    okno.fill((255,255,255))
    doors.render(okno)
    pygame.display.update()