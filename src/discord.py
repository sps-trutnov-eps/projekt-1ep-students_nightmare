import pygame as pg
from pygame import mixer

class Discord():
    eventon = False

    def __init__(self, dc_sizeX, dc_sizeY, dc_posX, dc_posY, surface, death_time):
        
        mixer.init()

        self.death_time = death_time
        self.dc_sizeX = dc_sizeX
        self.dc_sizeY = dc_sizeY
        self.dc_posX = dc_posX
        self.dc_posY = dc_posY
        self.surface = surface
        self.dc_pos = self.dc_posX, self.dc_posY
        self.eventon = False
        self.eventtype = None
        self.zmacknuto = False
        self.dead = False
        self.death_counter = 0

        self.sound_1 = pg.mixer.Sound("obj/discord/sounds/callvibrate.wav")
        self.sound_2 = pg.mixer.Sound("obj/discord/sounds/zprava.wav")

        self.callimage = pg.image.load("obj/discord/callimage.png")
        self.msgimage = pg.image.load("obj/discord/msgimage.png")
        self.callimage = pg.transform.scale(self.callimage, (dc_sizeX, dc_sizeY))
        self.msgimage = pg.transform.scale(self.msgimage, (dc_sizeX, dc_sizeY))

    def show(self):
        if self.zmacknuto == False:
            if self.eventtype == "call":
                self.surface.blit(self.callimage, self.dc_pos)
                self.eventon = True
            if self.eventtype == "message":
                self.surface.blit(self.msgimage, self.dc_pos)
                self.eventon = True

    def event(self, randnum):
        if self.eventon == False:
            if randnum >= 30 and randnum <= 35:
                self.eventtype = "call"
                self.zmacknuto = False
                self.sound_1.play()
                randnum = 0
            if randnum >= 75 and randnum <= 80:
                self.eventtype = "message"
                self.zmacknuto = False
                self.sound_2.play()
                randnum = 0
        
    def detect(self, mousepos, mousepress):
        if self.eventon == True:
            self.death_counter += 1
            if self.death_counter == self.death_time:
                self.death = True
                return(self.death)
            if mousepos[0] > self.dc_posX and mousepos[0] < (self.dc_posX + self.dc_sizeX):
                if mousepos[1] > self.dc_posY and mousepos[1] < (self.dc_posY + self.dc_sizeY):
                    if mousepress[0] == True:
                        self.zmacknuto = True
                        self.eventon = False
                        self.death_counter = 0