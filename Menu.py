import time
import pygame
from pygame.locals import *
from Global import *
from Opening import *
class Menu(Opening):
    def OpeningScene(self, screen):
    	screen.blit(menu, (0,0))
        select_exit = Opening(menu_exit_1, menu_exit_2, (380, 500))
        select_help = Opening(help1, help2, (380, 600))
    	self.render()
        select_exit.render()
        time.sleep(0.05)
    	for event in pygame.event.get():
            if event.type == pygame.QUIT or (select_exit.isOver() and pygame.mouse.get_pressed()[0]):
            	pygame.quit()
            	exit()
            if (self.isOver() and pygame.mouse.get_pressed()[0]) or pygame.key.get_pressed()[K_ESCAPE] :
            	stage_num = 2
                time.sleep(0.1)
                return stage_num
        pygame.display.update()
        return 3
