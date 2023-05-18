import random
import pygame
import time
pygame.init()
X,Y = 800,600
x, y, w, h = 400, 300, 50, 50
tlacitko_x, tlacitko_y, tlacitko_w, tlacitko_h = 300,300 ,50 ,50
tlacitko_r, tlacitko_g, tlacitko_b = 0,255,0
dvere_r,dvere_g,dvere_b = 0,255,0

ucitel_u_dveri = False

okno = pygame.display.set_mode((X, Y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if random.randint(0, 1000) < 2 and not ucitel_u_dveri:
        ucitel_u_dveri = True
        cas_ucitel = pygame.time.get_ticks() / 1000
        cas_jumpscare = 6
        print(cas_ucitel)
  
        
    else:
        pass
    
    mouse = pygame.mouse.get_pos()
    mp = pygame.mouse.get_pressed(num_buttons=3)
    
    mys_vodorovne = mouse[0] >= tlacitko_x and mouse[0] <= tlacitko_x+tlacitko_w
    mys_svisle = mouse[1] >= tlacitko_y and mouse[1] <= tlacitko_y+tlacitko_h
    mys_na_tlacitku = mys_vodorovne and mys_svisle
    mys_stisk = mp[0]
    tlacitko_stisknute = mys_na_tlacitku and mys_stisk
    # tlacitko
    if tlacitko_stisknute:
        tlacitko_r,tlacitko_g,tlacitko_b = 255,0,0
    else:
        tlacitko_r,tlacitko_g,tlacitko_b = 0,255,0

    # dvere
    if not tlacitko_stisknute and not ucitel_u_dveri:
        dvere_r,dvere_g,dvere_b = 0,255,0
    elif not tlacitko_stisknute and ucitel_u_dveri:
        dvere_r,dvere_g,dvere_b = 0,0,255
    elif tlacitko_stisknute:
        dvere_r,dvere_g,dvere_b = 255,0,0
    if ucitel_u_dveri:
        cas_ted = pygame.time.get_ticks() / 1000
        if cas_ted - cas_ucitel >= cas_jumpscare:
            print("fatty")
    if ucitel_u_dveri and tlacitko_stisknute:
        ucitel_u_dveri = False 
    
    okno.fill((255,255,255))
    pygame.draw.rect(okno, (dvere_r,dvere_g,dvere_b), (x, y, w, h))
    pygame.draw.rect(okno, (tlacitko_r, tlacitko_g, tlacitko_b), (tlacitko_x,tlacitko_y,tlacitko_w,tlacitko_h))
    pygame.display.update()