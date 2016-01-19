import pygame
from pygame.locals import *
from Player import Player
from Img import *

class Shoe:
    image_x = 32
    image_y = 32

    #default speed increase = 1
    #default value of image_names is for TEST ONLY
    def __init__(self, image_names = bomb_image, speed = 1):
    	temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(temp, (self.image_x, self.image_y))
        self.speed = speed

    def GetSpeed(self):
        return self.speed

    def SetSpeed(self):
        self.speed = speed

    def GetImage(self):
        return self.image

    def Use(self, player):
        player.speed += speed

    
