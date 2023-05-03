import pygame, time, random, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Knife Hit")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# HODNOTY (screen/stump/knife)

   # Screen
width = 640
height = 960

   # Stump
stump_x = 310
stump_y = 252
stump_angle = 0

   # Knife
knife_x = 220
knife_y = 670

# IMAGES (background/stump/knife)

 # knife
knife_img = pygame.image.load("Images/knife.png")
knife_rect = knife_img.get_rect()

 # stump
stump_img = pygame.image.load("Images/stump.png")
stump_rect = stump_img.get_rect()
stump_rect.center = (stump_x, stump_y)

 # Background
window = pygame.display.set_mode((width,height))
background_img = pygame.image.load("Images/background.jpg")
background_img = pygame.transform.scale(background_img,(width,height))

last_time = pygame.time.get_ticks()

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background_img, (0, 0))
    screen.blit(knife_img, (knife_x, knife_y))
    
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - last_time
    
    # Rotace pařezu
    stump_angle += 300 * time_elapsed / 1000
    if stump_angle >= 360:
        stump_angle = 0
    
    stump_img_rotated = pygame.transform.rotate(stump_img, stump_angle)
    stump_rect = stump_img_rotated.get_rect(center=stump_rect.center)
    screen.blit(stump_img_rotated, stump_rect)

    pygame.display.update()
    
    last_time = current_time

pygame.quit()
        
    
    