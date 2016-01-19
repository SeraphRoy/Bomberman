import pygame
from pygame.locals import *
from sets import Set

class Block:
    image_x = 32
    image_y = 32

    #posSet is a set of positions, e.g. [(2,1), (4,3)]
    def __init__(self, image_name, posSet):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transfrom.scale(temp, (self.image_x, self.image_y))
        self.posSet = set(posList)

    def SetImage(self, image_name):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transfrom.scale(temp, (self.image_x, self.image_y))

    def SetSet(self, posSet):
        self.posSet = set(posSet)
        
    def GetImage(self):
    	return self.image

    def GetSet(self):
    	return self.posSet

    def AddBlock(self, pair):
    	self.posSet.add(pair)

    def RemoveBlcok(self, pair):
    	self.posSet.discard(pair)

    def GetNumBlock(self):
        return len(self.posSet)

    def ClearBlock(self):
        self.posSet.clear()
