import  pygame
import sys


class Tablet:
    
    def __init__(self):
        self.showed = False
    
    
    def toggle(self):
        if self.showed:
            # Add showing tablet
            self.showed=False 
        else: self.showed=True