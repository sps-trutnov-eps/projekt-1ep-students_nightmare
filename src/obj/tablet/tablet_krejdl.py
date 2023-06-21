import random
import pygame
import time
import random


class Tablet:
    def __init__(self):
        self.pozice_ucitele = [True, False, False, False]
    
    def posunout(self):
        ucitel_sance = random.randint(0,50)
        if ucitel_sance == 48:
            if self.pozice_ucitele == [True, False, False, False]:
                self.pozice_ucitele = [False, True, False, False]
                
            elif self.pozice_ucitele == [False, True, False, False]:
                self.pozice_ucitele = [False, False, True, False]
                
            elif self.pozice_ucitele == [False, False, True, False]:
                self.pozice_ucitele = [False, False, False, True]
                
            elif self.pozice_ucitele == [False, False, False, True]:
                self.pozice_ucitele = [False, False, False, False]
            
        
        
        
    def vykreslit(self, window):
        x = 250
        for camery in self.pozice_ucitele:
            x += 50
            if camery:
                pygame.draw.rect(window,(255,0,0), (x, 50, 50,50))
                
            else:
                pygame.draw.rect(window,(0,255,0), (x, 50,50,50))
        
        