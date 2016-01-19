import pygame
from pygame.locals import *
from Player import Player
from Img import *

class BombDmg:
    image_x = 32
    image_y = 32

    #default bomb damage increase = 1
    #default image_names value is for TEST ONLY
    def __init__(self, image_names = bomb_image, bombdmg = 1):
    	temp = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(temp, (self.image_x, self.image_y))
        self.bombdmg = bombdmg

    def GetBombdmg(self):
        return self.bombdmg

    def SetBombdmg(self):
        self.bombdmg = bombdmg

    def GetImage(self):
        return self.image

    def Use(self, player):
        player.bomb_damage += bombdmg

    
