import pickle
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
from Boss import Boss

#re-initialize the game
def GameReinitialization(stage_num):
         global enemys, all_enemies, p
	 p = Player(player_images,bomb_image,150,10,20,1,2,hp_image)
	 Item.pos = {}
	 toolbar.dict = {}
         enemys.clear()
	 for i in range(10):
		  item_x = random.randint(0,14)
		  item_y = random.randint(0,12)
		  Item(item_x,item_y,item_images)

         for i in range(stage_num/5):
                  g = Ghost(random.randint(50,730), random.randint(50,730),50,150, ghost_images, 200,200)
                  d = Duck(random.randint(50, 730), random.randint(50,730), 50,150, duck_images,250,250)
                  enemys.add(g)
                  enemys.add(d)
                  all_enemies.add(g)
                  all_enemies.add(d)

         for i in range(stage_num/6):
                  m = Mage(random.randint(50,730), random.randint(50,730),50,150, mage_images, 300,300)
                  enemys.add(m)
                  all_enemies.add(m)

         for i in range(stage_num/7):
                  b = Boss(random.randint(50,730), random.randint(50,730),50,150, player_images, 200,200)
                  enemys.add(b)
                  all_enemies.add(b)


pygame.init()
p = Player(player_images,bomb_image,150,10,20,1,2,hp_image)
e1 = Ghost(256,256,50,150, ghost_images, 200,200)
all_enemies = pygame.sprite.Group()
all_enemies.add(e1)
enemys = {e1}
GameReinitialization(11)

## generate 10 items randomly
for i in range(10):
	 item_x = random.randint(0,14)
	 item_y = random.randint(0,12)
	 Item(item_x,item_y,item_images)

while True:
		ending = Ending(back_to_main_1, back_to_main_2, (390, 350))
                flag = False
                for e in enemys:
                         if e.CheckAlive() == True:
                                  flag = True
                                  break
                if not flag:
                         stage_num += 3
                         pickle.dump(stage_num, open("save_file", "wb"))
                         GameReinitialization(stage_num)

		if p.CheckAlive() == False and stage_num >= 11:
                                GameReinitialization(stage_num)
				stage_num = ending.OpeningScene(screen)
                                p.SetAlive(True)
				## reinitialize the game


		opening = Opening(upimage, downimage, (380,400))
		mode_select = SelectMode(new_game1, new_game2, (380,200))
		menu = Menu(back1, back2, (70, 30))
		if stage_num == 0:
				stage_num = opening.OpeningScene(screen)
                                clock.tick()
		elif stage_num == 1:
				stage_num = mode_select.OpeningScene(screen)
                                #GameReinitialization(stage_num)
                                clock.tick()
                                #print stage_num
		elif stage_num == 3:
				stage_num = menu.OpeningScene(screen)
                                clock.tick()
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
				if type(e) is not Boss:
					e.LiveAction(screen, p, current_time)
				else:
					e.LiveAction(screen, p, current_time,bomb_map)


			 collectItem(p)
			 toolbar.draw(screen)

			 #Reset current time
			 current_time = 0.0

			 pygame.display.update()

