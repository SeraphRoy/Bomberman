import pygame
import pickle
from pygame.locals import *
from Global import *
from Opening import *
class SelectMode(Opening):

    #overwrite it for mode-selection
    def OpeningScene(self, screen):
    	screen.blit(opening_bg, (0,0))
        select_exit = Opening(exit_1, exit_2, (380, 500))
        load_game = Opening(load_game1, load_game2, (380, 350))
    	self.render()
        select_exit.render()
        load_game.render()
    	for event in pygame.event.get():
            if event.type == pygame.QUIT or (select_exit.isOver() and pygame.mouse.get_pressed()[0]):
            	pygame.quit()
            	exit()
            if self.isOver() and pygame.mouse.get_pressed()[0]:
            	stage_num = 11
                return stage_num
            if load_game.isOver() and pygame.mouse.get_pressed()[0]:
            	stage_num = pickle.load(open("save_file", "rb"))
                return stage_num

        pygame.display.update()
        return 1
