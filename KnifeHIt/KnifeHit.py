import pygame, time, random, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Knife Hit")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# HODNOTY (screen/stump/knife/knife_bullet/knifes/Timer/Colors)

   # Screen
width = 640
height = 960

   # Stump
stump_x = 310
stump_y = 252
stump_angle = 0
stump_rotation_speed = 1

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

   # Timer
timer_x = 10
timer_y = 10
timer_width = 100
timer_height = 20

   # Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

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

game_time = 20
start_ticks = pygame.time.get_ticks()

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background_img, (0, 0))
    screen.blit(knife_img, (knife_x, knife_y))
    
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - last_time
    keys = pygame.key.get_pressed()
    
    time_left = max(0, game_time - (pygame.time.get_ticks() - start_ticks) // 1000)
    line_width = time_left / game_time * timer_width
    pygame.draw.line(screen, red, (timer_x, timer_y), (timer_x + line_width, timer_y), timer_height)

    font = pygame.font.Font(None, 24)
    text = font.render(f"Time left: {time_left}", True, black)
    screen.blit(text, (timer_x, timer_y + timer_height + 5))
 
    if keys[K_SPACE]:
        current_time = time.time()
        if current_time - last_space_press > 0.7:
            knifes.append([knife_x + knife_rect.width//3 - knife_bullet_x//5.3, knife_y])
            last_space_press = current_time
    for knife in knifes:
        knife[1] += knife_speed
        window.blit(pygame.transform.scale(knife_bullet_img, (knife2_x, knife2_y)), knife)
              
    stump_angle += stump_rotation_speed 
    if stump_angle >= 360:
        stump_angle = 0
        
    stump_img_rotated = pygame.transform.rotate(stump_img, stump_angle)
    stump_rect = stump_img_rotated.get_rect(center=stump_rect.center)
    screen.blit(stump_img_rotated, stump_rect)
    
    for knife in knifes:
        if knife[1] < stump_y and knife[1] + knife2_y > stump_y:
            if stump_x - knife2_x/2 < knife[0] < stump_x + knife2_x/2:
                knife_speed = 0
                knife[1] = stump_y - 1 
      
    if time_left <= 0:
        running = False
    pygame.display.update()
    
    last_time = current_time

pygame.quit()
        
    
    