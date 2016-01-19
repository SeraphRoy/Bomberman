import pygame
from pygame.locals import *
from Player import Player

class NumBomb:
    image_x = 32
    image_y = 32

    #default num of bomb increase = 1
    def __init__(self, image_names, bomb = 1):
    	temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(temp, (self.image_x, self.image_y))
        self.bomb = bomb

    def GetBomb(self):
        return self.bomb

    def SetBomb(self):
        self.bomb = bomb

    def GetImage(self):
        return self.image

    def Use(self, player):
        player.max_bomb += bomb

    
