import pygame
import pygame.locals
from pygame.locals import *
from sets import Set
from Img import *

class Block:
    image_x = 32
    image_y = 32

    #posSet is a set of positions, e.g. [(2,1), (4,3)]
    #default value of image_name is for TEST ONLY
    def __init__(self, image_name, posSet = []):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(temp, (self.image_x, self.image_y))
        self.posSet = set(posSet)

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

    def PutsOnScreen(self, screen):
        for point in self.posSet:
            screen.blit(self.image, point)

            
