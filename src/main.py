import pygame
pygame.init()

    # Game Window's variables
screen_width = 1920
screen_height = 1080

# Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    # Easily exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
               
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE  :
            exit()