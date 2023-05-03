import pygame, time, random, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Knife Hit")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# HODNOTY (screen)

   # Screen
width = 640
height = 960

# IMAGES (background)

 # Background
window = pygame.display.set_mode((width,height))
background_img = pygame.image.load("Images/background.jpg")
background_img = pygame.transform.scale(background_img,(width,height))

running = True 
while running:
    
    window.blit(background_img,(0,0))
    
    
    pygame.display.update()
    
    
    
pygame.quit()