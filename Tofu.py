import pygame
from pygame.locals import *
from random import randint
from Shoe import Shoe
from sets import Set 
from NumBomb import NumBomb
from BombDmg import BombDmg
from Img import *
from Object import *
from Item import *

class Tofu(Object):
    # Type num = 3
    def __init__(self,image=block_image,x_index=5,y_index=5):
        super(Tofu,self).__init__(False,3,block_image,x_index*OBJECT_X,y_index*OBJECT_Y)
        self.isContainItem = randint(0,1)
        if (self.isContainItem == 1):
            self.itemType = random.randint(1,7)
            self.item =  self.GenerateItem(self.itemType)
        #elif (self.isContainItem == 0):
        #    self.item = Object(True,0,transparent_image)
    def GenerateItem(self,rand):
        #if rand == 0:
        #    return Object(True,0,transparent_image,self.GetX(),self.GetY())
        if rand == 1:
            return Nike(self.x_Index,self.y_Index)
        if rand == 2:
            return Low_speed_field(self.x_Index,self.y_Index)
        if rand == 3:
            return Sadako(self.x_Index,self.y_Index)
        if rand == 4:
            return Heart(self.x_Index,self.y_Index)
        if rand == 5:
            return Tool1(self.x_Index,self.y_Index)
        if rand == 6:
            return Tool2(self.x_Index,self.y_Index)
        if rand == 7:
            return Stimpack(self.x_Index,self.y_Index)
    def Explode(self):
        self.image = burst
        self.type = 4
        if self.isContainItem == 0:
            self.type = 0
'''
    def GetItemImage(self,itemType):
        if itemType == 1:
            return nike_image
        if itemType == 2:
            return low_speed_image
        if itemType == 3:
            return sadako_image
        if itemType == 4:
            return heart_image
        if itemType == 5:
            return tool1_image
        if itemType == 6:
            return tool2_image
        if itemType == 7:

    def SwitchToItem(self):
    # Type num for item = 4
        self.type = 4
        temp = self.GenerateItem(self.itemType)
        self.currentImage = temp.GetImage()
        self.nextImage = transparent
        self.time = 1000000
'''      
        