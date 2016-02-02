from Player import Player
from Img import *
import pygame
from pygame.locals import *
from sys import exit
import Block
from Block import Block
from Bomb import BombMatrix
from Enemy import Enemy
from Ghost import Ghost
from Item import *
import random
from Opening import *
from Global import *
from SelectMode import *
pygame.init()

while True:
    if p.CheckAlive() == False:
      break;
    opening = Opening(upimage, downimage, (380,400))
    adventure_mode = SelectMode(adventure_mode1, adventure_mode2, (380,400))
    if stage_num == 0:
   	stage_num = opening.OpeningScene(screen)
    elif stage_num == 1:
        stage_num = adventure_mode.OpeningScene(screen)
    else:
       time_passed = clock.tick()
       time_passed_seconds = time_passed / 1000.0
       current_time+=time_passed_seconds


       if current_time<total_time:
           continue
                    
       for event in pygame.event.get():
           if event.type == QUIT:
               exit()

       screen.blit(background, (0,0))

       bomb_map.CheckAllBombs(screen,current_time,X_INDEX,Y_INDEX,burst)

       for i in item_pos:
           item_pos[i].draw(screen)

       pressed_Key = pygame.key.get_pressed()

       blocks.PutsOnScreen(screen)

       #third argument pass how many time hada passed since last tiem
       p.Action(screen,pressed_Key,current_time, bomb_map)

       for e in enemys:
            e.Action(screen, p, current_time)
       collectItem(p)

       #Reset current time
       current_time = 0.0

       pygame.display.update()

screen.blit(gameover, (290,250))
pygame.display.update()
while True:
  for event in pygame.event.get():
           if event.type == QUIT:
               exit()

