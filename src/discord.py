import pygame as pg

class Discord():
    eventon = False

    def __init__(self, dc_sizeX, dc_sizeY, dc_posX, dc_posY, surface):

        self.dc_sizeX = dc_sizeX
        self.dc_sizeY = dc_sizeY
        self.dc_posX = dc_posX
        self.dc_posY = dc_posY
        self.surface = surface
        self.dc_pos = self.dc_posX, self.dc_posY
        self.eventon = False
        self.eventtype = None

        self.callimage = pg.image.load("icucall.png")
        self.msgimage = pg.image.load("icumsg.png")
        self.callimage = pg.transform.scale(self.callimage, (dc_sizeX, dc_sizeY))
        self.msgimage = pg.transform.scale(self.msgimage, (dc_sizeX, dc_sizeY))

    def show(self):
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
            if randnum >= 75 and randnum <= 80:
                self.eventtype = "message"