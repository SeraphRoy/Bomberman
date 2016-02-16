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
from Duck import Duck
from Mage import Mage
from Item import *
import random


clock = pygame.time.Clock()

screen = pygame.display.set_mode((768,768),0,32)

background = pygame.image.load(back_ground_name).convert()
bomb = pygame.image.load(bomb_image).convert_alpha()
bomb = pygame.transform.scale(bomb, (51,51))
burst = pygame.image.load(burst_iamge).convert_alpha()
burst = pygame.transform.scale(burst,(64,59))
item_images = [nike_image, low_speed_image, sadako_image, heart_image,
               tool1_image, tool2_image, stimpack_image]


player_images = [player_up1,player_up2,player_up3,player_up4,
                 player_down1,player_down2,player_down3,player_down4,
                 player_left1,player_left2,player_left3,player_left2,
                 player_right1,player_right2,player_right3,player_right4]

ghost_images = [ghost_up1,ghost_up2,ghost_up3,ghost_up4,
				ghost_down1, ghost_down2,ghost_down3,ghost_down4,
				ghost_left1, ghost_left2, ghost_left3, ghost_left4,
				ghost_right1,ghost_right2,ghost_right3,ghost_right4]

duck_images = [duck_up1,duck_up2,duck_up3,duck_up4,
			   duck_down1,duck_down2,duck_down3,duck_down4,
			   duck_left1,duck_left2,duck_left3,duck_left4,
			   duck_right1,duck_right2,duck_right3,duck_right4]

mage_images = [mage_up1,mage_up2,mage_up3,mage_up4,
			   mage_down1,mage_down2,mage_down3,mage_down4,
			   mage_left1,mage_left2,mage_left3,mage_left4,
			   mage_right1,mage_right2,mage_right3,mage_right4]



setOfBlocks = [(100,100), (240,240), (49, 203), (500, 20), (668, 100)]
all_blocks = pygame.sprite.Group()
for point in setOfBlocks:
   block = Block(block_image, point[0], point[1])
   all_blocks.add(block)

X_INDEX = 13
Y_INDEX = 15

bomb_map = BombMatrix(X_INDEX,Y_INDEX)
total_time = 0.05
current_time = 0.0
exploded_queue = []


stage_num = 0
opening_bg = pygame.image.load(open_image).convert()
gameover   = pygame.image.load(gameover_image).convert()
normal_face = pygame.image.load(normal_face_image).convert()
hurt_face = pygame.image.load(hurt_face_image).convert()
dead_face = pygame.image.load(dead_face_image).convert()
menu = pygame.image.load(menu).convert()
#back1 = pygame.image.load(back1).convert()
#back2 = pygame.image.load(back2).convert()
#help1 = pygame.image.load(help1).convert()
#help2 = pygame.image.load(help2).convert()
#menu_exit_1 = pygame.image.load(menu_exit_1).convert()
#menu_exit_2 = pygame.image.load(menu_exit_2).convert()
