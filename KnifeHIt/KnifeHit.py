import pygame, time, random, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Knife Hit")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# HODNOTY (screen/stump)

   # Screen
width = 640
height = 960
   # Stump
stump_x = 310
stump_y = 252
stump_angle = 0

# IMAGES (background/stump)

 # stump
stump_img = pygame.image.load("Images/stump.png")
stump_rect = stump_img.get_rect()
stump_rect.center = (stump_x, stump_y)

 # Background
window = pygame.display.set_mode((width,height))
background_img = pygame.image.load("Images/background.jpg")
background_img = pygame.transform.scale(background_img,(width,height))

running = True 
while running:
    
    window.blit(background_img,(0,0))
    stump_img_rotated = pygame.transform.rotate(stump_img, stump_angle)
    stump_rect = stump_img_rotated.get_rect(center=stump_rect.center)
    window.blit(stump_img_rotated, stump_rect)

       
    stump_angle += 1
    if stump_angle >= 360:
        stump_angle = 0

        
    
    
    pygame.display.update()
    
    
    
pygame.quit()