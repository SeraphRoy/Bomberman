import pygame
from pygame.locals import *

class Bomb:
    image_x = 32
    image_y = 32
    
    def __init__(self,image_name, x, y):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(temp,(self.image_x,self.image_y))
        self.time = 2.0
        self.x = x
        self.y = y

    def TimePassed(self,t):
        self.time-=t
        if self.time<=0:
            return True
        else:
            return False

    def GetImage(self):
        return self.image

    def SetX(self,x):
        self.x = x

    def SetY(self,y):
        self.y = y

    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y
    
