import pygame
from pygame.locals import *
from Img import *
from Global import *


class Opening(object):

    def __init__(self, upimage, downimage, position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position

    def isOver(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2

        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            screen.blit(self.imageDown, (x-w/2, y-h/2))

        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
                        
    def OpeningScene(self, screen):
    	screen.blit(opening_bg, (0,0))
    	self.render()
    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	pygame.quit()
            	exit()
            if self.isOver() and pygame.mouse.get_pressed()[0]:
            	stage_num = 1
                return stage_num
        pygame.display.update()
        return 0
	


