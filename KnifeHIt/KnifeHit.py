import pygame, time, random, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Knife Hit")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# HODNOTY (screen/stump/knife/knife_bullet/knifes)

   # Screen
width = 640
height = 960

   # Stump
stump_x = 310
stump_y = 252
stump_angle = 0

   # Knife
knife_x = 250
knife_y = 685

   # Knife2
knife2_x = 141
knife2_y = 200

   # Knife_bullet
knifes = []
knife_speed = -2
knife_bullet_x = 250
knife_bullet_y = 685
last_space_press = 0


# IMAGES (background/stump/knife/knife_bullet)

 # knife
knife_img = pygame.image.load("Images/knife.png")
knife_rect = knife_img.get_rect()

 # stump
stump_img = pygame.image.load("Images/stump.png")
stump_rect = stump_img.get_rect()
stump_rect.center = (stump_x, stump_y)

 # background
window = pygame.display.set_mode((width,height))
background_img = pygame.image.load("Images/background.jpg")
background_img = pygame.transform.scale(background_img,(width,height))

 # knife
knife_bullet_img = pygame.image.load("Images/knife2.png") 

last_time = pygame.time.get_ticks()

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background_img, (0, 0))
    screen.blit(knife_img, (knife2_x, knife2_y))
    
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - last_time
    keys = pygame.key.get_pressed()

    
    
    if keys[K_SPACE]:
        current_time = time.time()
        if current_time - last_space_press > 0.7:
            knifes.append([knife_x + knife_rect.width//3 - knife_bullet_x//5.3, knife_y])
            last_space_press = current_time
    for knife in knifes:
        knife[1] += knife_speed
        window.blit(pygame.transform.scale(knife_bullet_img, (knife2_x, knife2_y)), knife)
        
        
    
# Rotace pařezu
     
    stump_angle += 60000 * time_elapsed / 1000
    if stump_angle >= 360:
        stump_angle = 0
        
    stump_img_rotated = pygame.transform.rotate(stump_img, stump_angle)
    stump_rect = stump_img_rotated.get_rect(center=stump_rect.center)
    screen.blit(stump_img_rotated, stump_rect)
    
        
    
    
   
    

    pygame.display.update()
    
    last_time = current_time

pygame.quit()
        
    
    