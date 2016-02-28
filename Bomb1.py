import pygame
from pygame.locals import *
from Object import *
from Img import *

class Bomb(Object):
    OBJECT_X = 51
    OBJECT_Y = 51
    transparent = pygame.transform.scale(pygame.image.load(transparent_image),(OBJECT_X,OBJECT_Y))
    
    def __init__(self,x,y,image,damageLength=1):
        super(Bomb,self).__init__(False,1,image,x,y)
        #print ("place bomb")
        self.damageLength = damageLength
        self.time = 2.0
    
    def TimePassed(self,t):
        self.time-=t
        if self.time<=0:
            return True
        else:
            return False
    
    def SetDamageLength(self,damageLength):
        self.damageLength = damageLength

    def IncrDamageLength(self):             
        self.damageLength += 1   
        
    def GetDamageLength(self):
        return self.damageLength


             
    #def Update(self):
       #super(Bomb, self).Update()
        #self = Object(True,0,transparent_image,transparent_image)
        
        # need to trigger local bombs
        # I think we should still use recurrsion even though we can now use iteration
        # to trigger bombs based on the type(int)
        # Because python does not offer passing by reference
'''
    def Update(self,time):
        if self.type == 5:
            self.isNull = True
            return
        if self.TimePassed(time):
            self.image = self.SetImage(burst_image)
            self.type = 5
'''