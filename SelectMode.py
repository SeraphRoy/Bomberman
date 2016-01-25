import pygame
from pygame.locals import *
from Global import *
from Opening import *
class SelectMode(Opening):
    def OpeningScene(self, screen):
    	screen.blit(opening_bg, (0,0))
    	self.render()
    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	pygame.quit()
            	exit()
            if self.isOver() and pygame.mouse.get_pressed()[0]:
            	stage_num = 2
                return stage_num
        pygame.display.update()
        return 1
