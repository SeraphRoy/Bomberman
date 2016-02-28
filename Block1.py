import pygame
import pygame.locals
from pygame.locals import *
from sets import Set
from Img import *
from Object import *

class Block(Object):

    # nextImage for Block should be a image of an item
    
    def __init__(self,blockImage,x_index,y_index):
        super(Block,self).__init__(False,2,blockImage,x_index*OBJECT_X,y_index*OBJECT_Y)
        
    def Explode(self):
        pass