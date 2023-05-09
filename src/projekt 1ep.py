import pygame
pygame.init()
X,Y = 800,600
x, y, w, h = 200, 300, 50, 50
r, g, b = 0, 255, 0
okno = pygame.display.set_mode((X, Y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    mouse = pygame.mouse.get_pos()
    
    if mouse[0] >= x and mouse[0] <= x+w and mouse[1] >= y and mouse[1] <= y+h:
        r,g,b = 255,0,0
    else:
        r,g,b = 0,255,0
    okno.fill((255,255,255))
    pygame.draw.rect(okno, (r, g, b), (x, y, w, h))
    pygame.display.update()