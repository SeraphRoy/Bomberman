import pygame
from pygame.locals import *
from Img import transparent_image

class Bomb:


    def __init__(self,image, x = -50, y = -50,damageLength = 1, isNull = False):
        BOMB_IMG_X = 51
        BOMB_IMG_Y = 51
        temp = pygame.image.load(image).convert_alpha()
        self.damageLength = 1
        self.image = pygame.transform.scale(temp,(BOMB_IMG_X,BOMB_IMG_Y))
        self.time = 2.0
        self.x_Index = int(x//BOMB_IMG_X)
        self.x = self.x_Index * BOMB_IMG_X
        self.y_Index = int(y//BOMB_IMG_Y)
        self.y = self.y_Index * BOMB_IMG_Y
        self.isNull = isNull
        

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

    def SetDamageLength(self,damageLength):
        self.damageLength = damageLength

    # Call this method when player recieved an increase-bomb-power item
    def IncrDamageLength(self):             
        self.damageLength += 1

    def GetDamageLength(self):
        return self.damageLength

    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y

    def GetX_Index(self):
        return self.x_Index

    def GetY_Index(self):
        return self.y_Index

    def IsNull(self):
        return self.isNull



class BombMatrix:

    def __init__(self,X_MAX=13,Y_MAX=15):
        self.X_MAX = X_MAX
        self.Y_MAX = Y_MAX
        self.null_Bomb = Bomb(transparent_image,-50,-50,0,True)
        self.bombMatrix = [[self.null_Bomb for x in range(X_MAX)] for y in range(Y_MAX)]

    def AddBomb(self, newBomb):
        self.bombMatrix[newBomb.GetX_Index()][newBomb.GetY_Index()] = newBomb

    def RemoveBomb(self,screen, x_Index, y_Index,burst):
        screen.blit(burst,(self.bombMatrix[y_Index][x_Index].GetX(),self.bombMatrix[y_Index][x_Index].GetY()))
        self.bombMatrix[y_Index][x_Index] = self.null_Bomb

        if (x_Index >= 1) and (self.bombMatrix[y_Index][x_Index-1].IsNull() == False):
            self.RemoveBomb(screen,x_Index-1,y_Index,burst)
        if (y_Index >= 1) and (self.bombMatrix[y_Index-1][x_Index].IsNull() == False):
            self.RemoveBomb(screen,x_Index,y_Index-1,burst)
        if (x_Index <= self.X_MAX-2) and (self.bombMatrix[y_Index][x_Index+1].IsNull() == False):
            self.RemoveBomb(screen,x_Index+1,y_Index,burst)
        if (y_Index <= self.Y_MAX-2) and (self.bombMatrix[y_Index+1][x_Index].IsNull() == False):
            self.RemoveBomb(screen,x_Index,y_Index+1,burst)

    def CheckAllBombs(self, screen, current_time, X_INDEX, Y_INDEX,burst):
        for x in range(X_INDEX):
            for y in range(Y_INDEX):
                if (self.bombMatrix[y][x].isNull == False) and (self.bombMatrix[y][x].TimePassed(current_time) == True):
                    self.RemoveBomb(screen,x,y,burst)
                else:
                   screen.blit(self.bombMatrix[y][x].GetImage(),(self.bombMatrix[y][x].GetX(),self.bombMatrix[y][x].GetY()))

