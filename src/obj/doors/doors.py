import random
import pygame
import time

ucitel_u_dveri = False

game_over = pygame.image.load('gameoverscreen.png')

class Doors:
    def __init__(self, tlacitko_rozmery, tlacitko_barva, dvere_rozmery):
        self.tlacitko_rozmery = list(tlacitko_rozmery)
        self.tlacitko_barva = list(tlacitko_barva)
        
        self.dvere_rozmery = list(dvere_rozmery)
        self.dvere_barva = 0,255,0
        
        self.tlacitko_stisknute = False
        self.ucitel_u_dveri = False
        
        self.game_over_happened = False 
        
    def sance_nastavit_ucitele(self):
        if not self.ucitel_u_dveri and random.randint(0, 1000) < 2:
            self.ucitel_u_dveri = True
            
            self.cas_ucitel = pygame.time.get_ticks() / 1000
            self.cas_jumpscare = 2 # sekund
        
    def kontrola_stisku_tlacitka(self):
        pozice_mysi = pygame.mouse.get_pos()
        
        mys_vodorovne = pozice_mysi[0] >= self.tlacitko_rozmery[0] and pozice_mysi[0] <= self.tlacitko_rozmery[0] + self.tlacitko_rozmery[2]
        mys_svisle = pozice_mysi[1] >= self.tlacitko_rozmery[1] and pozice_mysi[1] <= self.tlacitko_rozmery[1] + self.tlacitko_rozmery[3]
        mys_na_tlacitku = mys_vodorovne and mys_svisle
        
        mp = pygame.mouse.get_pressed(num_buttons=3)
        mys_stisk = mp[0]
        
        tlacitko_stisknute = mys_na_tlacitku and mys_stisk
        
        # tlacitko
        if tlacitko_stisknute:
            self.tlacitko_stisknute = True
            self.tlacitko_barva = 0,0,255
        else:
            self.tlacitko_stisknute = False
            self.tlacitko_barva = 0,255,0
            
            
    def odpocet_jumpscare(self,window):
        if not self.tlacitko_stisknute and self.ucitel_u_dveri:
            self.dvere_barva = 255,0,0           
            cas_ted = pygame.time.get_ticks() / 1000
            if cas_ted - self.cas_ucitel >= self.cas_jumpscare:
                window.blit(game_over,(0,0))
                self.game_over_happened = True
                
                
        elif self.tlacitko_stisknute and self.ucitel_u_dveri:
            self.ucitel_u_dveri = False
            
            self.dvere_barva = 0,0,255
        else:
            self.dvere_barva = 0,255,0
            
    def vykreslit(self, window):
        pygame.draw.rect(window, self.dvere_barva, self.dvere_rozmery)
        pygame.draw.rect(window, self.tlacitko_barva, self.tlacitko_rozmery)