import pygame
from pygame.locals import *
from random import randint
from Shoe import Shoe
from sets import Set 
from NumBomb import NumBomb
from BombDmg import BombDmg
from Img import *

def randItem(randNum):
    switcher = {
        0: Shoe(),
        1: NumBomb(),
        2: BombDmg(),
        }
    return switcher.get(randNum)

class Tofu:
    image_x = 32
    image_y = 32

    #posSet is a set of positions, e.g. [(2,1), (4,3)]
    def __init__(self, image_name, x, y):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transfrom.scale(temp, (self.image_x, self.image_y))
        temp = randint(0,1)
	#0<->shoe, 1<->numbomb, 2<->bombdmg
        if(temp):
            temp = randint(0,2)
            self.item = randItem(temp)
            self.isItem = true
        else:
            self.isItem = false
	self.x = x
        self.y = y
        

    def SetImage(self, image_name):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transfrom.scale(temp, (self.image_x, self.image_y))

    def SetX(self, x):
        self.x = x

    def SetY(self, y):
        self.y = y
    
    def SetItem(self, item):
        self.item = item
        self.isItem = true

    def GetItem(self):
    	return self.item

    def GetX():
    	return self.x

    def GetY():
        return self.y
        
    def GetImage(self):
    	return self.image



