import time
from Player import Player
from Img import *
import pygame
from pygame.locals import *
from sys import exit
import Block
from Block import Block
from Ending import Ending
from Bomb import BombMatrix
from Enemy import Enemy
from Ghost import Ghost
from Item import *
import random
from Opening import *
from Global import *
from SelectMode import *
from Menu import *
pygame.init()

p = Player(player_images,bomb_image,150,10,20,1,2,hp_image)
e1 = Ghost(256,256,50,150, ghost_images, 200,200)
e2 = Duck(512,256,50,150, duck_images, 250,250)
e3 = Mage(400,220,50,50, mage_images, 300, 300)
all_enemies = pygame.sprite.Group()
all_enemies.add(e1)
all_enemies.add(e2)
all_enemies.add(e3)
enemys = {e1,e2,e3}

for i in range(10):
   item_x = random.randint(0,14)
   item_y = random.randint(0,12)
   Item(item_x,item_y,item_images)

while True:
    ending = Ending(back_to_main_1, back_to_main_2, (390, 350))
    if p.CheckAlive() == False and stage_num == 2:
        stage_num = ending.OpeningScene(screen)
        p = Player(player_images,bomb_image,150,10,20,1,2,hp_image)
        e1 = Ghost(256,256,50,150, ghost_images, 200,200)
        e2 = Duck(512,256,50,150, duck_images, 250,250)
        e3 = Mage(400,220,50,50, mage_images, 300, 300)
        enemys = {e1,e2,e3}
        Item.pos = {}
        toolbar.dict = {}
        for i in range(10):
            item_x = random.randint(0,14)
            item_y = random.randint(0,12)
            Item(item_x,item_y,item_images)

        
    opening = Opening(upimage, downimage, (380,400))
    mode_select = SelectMode(adventure_mode1, adventure_mode2, (380,200))
    menu = Menu(back1, back2, (70, 30))
    if stage_num == 0:
   	stage_num = opening.OpeningScene(screen)
    elif stage_num == 1:
        stage_num = mode_select.OpeningScene(screen)
    elif stage_num == 3:
        stage_num = menu.OpeningScene(screen)
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
       screen.blit(normal_face, (665, 665))
       bomb_map.CheckAllBombs(screen,current_time,X_INDEX,Y_INDEX,burst, p, 10, all_enemies)

       for i in Item.pos:
           Item.pos[i].draw(screen)

       pressed_Key = pygame.key.get_pressed()
       if pressed_Key[pygame.K_ESCAPE]:
           stage_num = 3

       for block in all_blocks:
           block.PutsOnScreen(screen)

       #third argument pass how many time hada passed since last tiem
       p.Action(screen,pressed_Key,current_time, bomb_map, all_blocks)

       for e in enemys:
            e.LiveAction(screen, p, current_time)

       collectItem(p)
       toolbar.draw(screen)
       
       #Reset current time
       current_time = 0.0

       pygame.display.update()

