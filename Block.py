import pygame
import pygame.locals
from pygame.locals import *
from sets import Set
from Img import *

class Block(pygame.sprite.Sprite):
    image_x = 51
    image_y = 51

    def __init__(self, image_name, x, y):
        pygame.sprite.Sprite.__init__(self)
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(temp, (self.image_x, self.image_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def SetImage(self, image_name):
        temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transfrom.scale(temp, (self.image_x, self.image_y))

    def GetImage(self):
    	return self.image

    def PutsOnScreen(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

            
