import random
import pygame
import time
pygame.init()

screen_X,screen_Y = 800, 600
mouse = pygame.mouse.get_pos()
mp = pygame.mouse.get_pressed(num_buttons=3)

#x, y, w, h = 400, 300, 50, 50
#tlacitko_x, tlacitko_y, tlacitko_w, tlacitko_h = 300, 300 ,50 ,50
#tlacitko_r, tlacitko_g, tlacitko_b = 0, 255 ,0
#dvere_r,dvere_g,dvere_b = 0, 255 ,0

class Tlacitko:
    def __init__(self, x):
        self.X = x
        self.Y = 300
        self.width = 50
        self.height = 50
        self.R = 0
        self.G = 255
        self.B = 0

class Mys:
    def __init__(self):
        tlacitko = Tlacitko(self)
        
        self.vodorovne = mouse[0] >= tlacitko.X and mouse[0] <= tlacitko.X + tlacitko.width
        self.svisle = mouse[1] >= tlacitko.Y and mouse[1] <= tlacitko.Y + tlacitko.height
        self.na_tlacitku = self.vodorovne and self.svisle
        self.stisk = mp[0]
        


class Dvere:
    def __init__(self):
        self.R = 0
        self.G = 255
        self.B = 0

ucitel_u_dveri = False

tlacitko_vlevo = Tlacitko(300)
tlacitko_vpravo = Tlacitko(400)

mys = Mys()

dvere = Dvere()

okno = pygame.display.set_mode((screen_X, screen_Y))


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
    


      
    if tlacitko.stisk:
        tlacitko.R,tlacitko.G,tlacitko.B = 255, 0, 0
         
    else:
         tlacitko.R,tlacitko.G,tlacitko.B = 0, 255, 0

    if not tlacitko_stisknute and not ucitel_u_dveri:
         dvere.r,dvere_g,dvere_b = 0,255,0
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