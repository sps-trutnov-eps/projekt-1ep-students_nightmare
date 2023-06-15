import random
import pygame
import time
ucitel_u_dveri = False



class Dvere:
    def __init__(self, mys, tlacitko_rozmery, tlacitko_barva, dvere_rozmery):
        self.mys_vodorovne = mys[0]
        self.mys_svisle = mys[1]
        self.tlacitko_rozmery = list(tlacitko_rozmery)
        self.tlacitko_barva = list(tlacitko_barva)
        self.dvere_rozmery = list(dvere_rozmery)
        self.dvere_barva = 0,255,0
        
        
        
    def ucitel_u_dveri(self):
        self.ucitel_u_dveri = False 
        if random.randint(0, 1000) < 2 and not ucitel_u_dveri:
            self.ucitel_u_dveri = True
            self.cas_ucitel = pygame.time.get_ticks() / 1000
            self.cas_jumpscare = 6 

        
        
    def get_pressed(self):
        self.get_pressed = False 
        mys_na_tlacitku = mys_vodorovne and mys_svisle
        mp = pygame.mouse.get_pressed(num_buttons=3)
        mys_stisk = mp[0]
        tlacitko_stisknute = mys_na_tlacitku and mys_stisk
        # tlacitko
        if tlacitko_stisknute:
            self.get_pressed = True 
        else:
            self.tlacitko_barva = 0,255,0
            
            
    def jumpscare(self):
        # dvere
        if self.get_pressed == False and self.ucitel_u_dveri:
            self.dvere_barva = 0,0,255
            self.cas_ted = pygame.time.get_ticks() / 1000
            if self.cas_ted - self.cas_ucitel >= self.cas_jumpscare:
                print("fatty")
        elif self.ucitel_u_dveri and self.get_pressed:
            ucitel_u_dveri = False
            self.tlacitko_barva = 0,0,255
            self.dvere_barva = 0,0,255
        else:
            self.tlacitko_barva = 0,255,0
            self.dvere_barva = 0,255,0
            
    def render(self, window):
        pygame.draw.rect(window, self.dvere_barva, self.dvere_rozmery)
        pygame.draw.rect(window, self.tlacitko_barva, self.tlacitko_rozmery)
         
