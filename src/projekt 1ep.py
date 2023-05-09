import pygame
pygame.init()
X,Y = 1920,1080
x, y, w, h = 200, 300, 50, 50
r, g, b = 0, 255, 0
okno = pygame.display.set_mode((X, Y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    mouse = pygame.mouse.get_pos()
    mp = pygame.mouse.get_pressed(num_buttons=3)
    
    if mouse[0] >= x and mouse[0] <= x+w and mouse[1] >= y and mouse[1] <= y+h and mp[0]:
        r,g,b = 255,0,0
    else:
        r,g,b = 0,255,0
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.button)
    
    okno.fill((255,255,255))
    pygame.draw.rect(okno, (r, g, b), (x, y, w, h))
    pygame.display.update()