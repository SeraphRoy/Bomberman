import pygame
from pygame.locals import *
from Img import *
from Global import *
from Opening import *

class Ending(Opening):

    def OpeningScene(self, screen):
        while True:
            screen.blit(gameover, (290, 150))
            select_exit = Opening(ending_exit_1, ending_exit_2, (390, 500))
            self.render()
            select_exit.render()
#            screen.blit(pygame.image.load(transparent_image).convert_alpha(), (655, 655))
            screen.blit(dead_face, (665, 665))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (select_exit.isOver() and pygame.mouse.get_pressed()[0]):
                    pygame.quit()
                    exit()
                if self.isOver() and pygame.mouse.get_pressed()[0]:
                    stage_num = 0
                    return stage_num
            pygame.display.update()                
