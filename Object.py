import pygame
from pygame.locals import *
from Img import *
from sys import *

OBJECT_X = 51
OBJECT_Y = 51
transparent = pygame.transform.scale(pygame.image.load(transparent_image),(OBJECT_X,OBJECT_Y))

class Object(pygame.sprite.Sprite):
    
    
    def __init__(self,isNull,objectType,currentImage,nextImage = transparent,x=-100,y=-100,):
        pygame.sprite.Sprite.__init__(self)
        

        
        self.time = 10000000
        self.isNull = isNull

        ''' Object Type
            0 = blank
            1 = Bomb
            2 = Block
            3 = item            
        '''
        self.type = objectType
        self.x = x
        self.y = y
        
        self.currentImage = pygame.transform.scale(pygame.image.load(currentImage).convert_alpha(),(OBJECT_X,OBJECT_Y))
        #if (self.isNull == True):
        #    self.nextImage = transparent
        #else:
        self.nextImage = pygame.transform.scale(pygame.image.load(nextImage).convert_alpha(),(OBJECT_X,OBJECT_Y))
        
        self.x_Index = int(x//OBJECT_X)
        self.y_Index = int(y//OBJECT_Y)
        self.rect = self.currentImage.get_rect()
        self.rect.x = self.x_Index * OBJECT_X
        self.rect.y = self.y_Index * OBJECT_Y
    
    def SetX(self,x):
        self.rect.x = x

    def SetY(self,y):
        self.rect.y = y

    def GetX(self):
        return self.rect.x
    
    def GetY(self):
        return self.rect.y

    def GetX_Index(self):
        return self.x_Index

    def GetY_Index(self):
        return self.y_Index

    def IsNull():
        return self.isNull
        
    def SetDamageLength(self,damageLength):
        self.damageLength = damageLength
        
    def Display(self, screen):
        screen.blit(self.currentImage, (self.rect.x, self.rect.y))
        
class ObjectMatrix:

    def __init__(self,X_MAX=13,Y_MAX=15):
        self.X_MAX = X_MAX
        self.Y_MAX = Y_MAX
        self.blank = Object(True,0,transparent_image,transparent_image)
        self.objectMatrix = [[self.blank for x in range(X_MAX)] for y in range(Y_MAX)]

    def Add(self,newObject):
        self.objectMatrix[newObject.GetY_Index()][newObject.GetX_Index()] = newObject
        #print "Displayed at X = "
        #print self.objectMatrix[newObject.GetY_Index()][newObject.GetX_Index()].rect.x
        #print " y = " 
        #print self.objectMatrix[newObject.GetY_Index()][newObject.GetX_Index()].rect.y

    def Update(self,screen,current_time):
        self.Display(screen)
        
    def Display(self,screen):
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                if (self.objectMatrix[y][x].isNull == False):
                    self.objectMatrix[y][x].Display(screen)

                    