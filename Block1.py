import pygame
import pygame.locals
from pygame.locals import *
from sets import Set
from Img import *
from Object import *

class Block(Object):

    # nextImage for Block should be a image of an item
    
    def __init__(self,blockImage,x,y):
        super(Block,self).__init__(False,1,blockImage,blockImage,x,y)
        #temp = pygame.image.load(image_name).convert_alpha()
        #self.image = pygame.transform.scale(temp, (self.image_x, self.image_y))


    #def SetImage(self, image_name):
    #    temp = pygame.image.load(image_name).convert_alpha()
    #    self.image = pygame.transfrom.scale(temp, (self.image_x, self.image_y))

    #def GetImage(self):
    #    return self.image

    # originally called PutsOnScreen
    #def Display(self, screen):
    #    screen.blit(self.currentImage, (self.rect.x, self.rect.y))