import pygame
from pygame.locals import *
from Img import transparent_image

class Bomb:


    def __init__(self,image, x = -50, y = -50,length = 2):
        BOMB_IMG_X = 50
        BOMB_IMG_Y = 50
        temp = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(temp,(BOMB_IMG_X,BOMB_IMG_Y))
        self.time = 2.0
        self.x_Index = int(x//BOMB_IMG_X)
        self.x = self.x_Index * BOMB_IMG_X
        self.y_Index = int(y//BOMB_IMG_Y)
        self.y = self.y_Index * BOMB_IMG_Y

        self.length = length



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

    def GetX_Index(self):
        #print self.x_Index
        #print self.x
        return self.x_Index

    def GetY_Index(self):
        #print self.y_Index
        #print self.y
        return self.y_Index

class BombMatrix:

    def __init__(self,X_MAX=13,Y_MAX=15):
        self.X_MAX = X_MAX
        self.Y_MAX = Y_MAX
        self.null_Bomb = Bomb(transparent_image,-50,-50)
        self.bombMatrix = [[self.null_Bomb for x in range(X_MAX)] for y in range(Y_MAX)]

    def AddBomb(self, newBomb):
        self.bombMatrix[newBomb.GetX_Index()][newBomb.GetY_Index()] = newBomb

    def RemoveBomb(self, x_Index, y_Index):
        self.bombMatrix[y_Index][x_Index] = self.null_Bomb
