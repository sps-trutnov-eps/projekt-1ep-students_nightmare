import random
import pygame
import time
ucitel_u_dveri = False

okno = pygame.display.set_mode((X, Y))

class dvere:
    def __init__(self,mys, tlacitko_rozmery, tlacitko_barva):
        self.mys_vodorovne = list(mys[0])
        self.mys_svisle = list(mys[1])
        self.tlacitko_x = list(tlacitko[0])
        self.tlacitko_y = list(tlacitko[1])
        self.tlacitko_w = list(tlacitko[2])
        self.tlacitko_h = list(tlacitko[3])
        self.tlacitko_r = list(tlacitko_barva[0])
        self.tlacitko_g = list(tlacitko_barva[0])
        self.tlacitko_b = list(tlacitko_barva[0])
        
        
        
    def ucitel_u_dveri(self):
        ucitel_u_dveri = False 
        if random.randint(0, 1000) < 2 and not ucitel_u_dveri:
            ucitel_u_dveri = True
            self.cas_ucitel = pygame.time.get_ticks() / 1000
            self.cas_jumpscare = 6 
        else:
            pass
        
        
    def get_pressed(self):
        mys_na_tlacitku = mys_vodorovne and mys_svisle
        mp = pygame.mouse.get_pressed(num_buttons=3)
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
