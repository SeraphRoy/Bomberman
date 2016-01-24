from Player import Player
from Img import *
import pygame
from pygame.locals import *
from sys import exit
import Block
from Block import Block
from Bomb import BombMatrix
from Enemy import Enemy
from Item import *
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((768,768),0,32)

background = pygame.image.load(back_ground_name).convert()
bomb = pygame.image.load(bomb_image).convert_alpha()
bomb = pygame.transform.scale(bomb, (32,32))
burst = pygame.image.load(burst_iamge).convert_alpha()
burst = pygame.transform.scale(burst,(64,59))
item_images = [nike_image,low_speed_image,sadako_image]


player_images = [player_up1,player_up2,player_up3,player_up4,
                 player_down1,player_down2,player_down3,player_down4,
                 player_left1,player_left2,player_left3,player_left2,
                 player_right1,player_right2,player_right3,player_right4]

p = Player(player_images,bomb_image,150,10,20,1,1)

e = Enemy(256,256,50,200, enemy, 300,300)


setOfBlocks = [(100,100), (52,52), (240,240), (49, 203), (500, 20)]
blocks = Block(block_image, setOfBlocks)

X_INDEX = 13
Y_INDEX = 15

bomb_map = BombMatrix(X_INDEX,Y_INDEX)
total_time = 0.05
current_time = 0.0
exploded_queue = []

for i in range(7):
   item_x = random.randint(0,14)
   item_y = random.randint(0,12)
   Item(item_x,item_y,item_images)


while True:    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    current_time+=time_passed_seconds


    if current_time<total_time:
        continue
                    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))

    for x in range(X_INDEX):
        for y in range(Y_INDEX):
            if bomb_map.bombMatrix[y][x].TimePassed(current_time) == True :
                screen.blit(burst,(bomb_map.bombMatrix[y][x].GetX(),bomb_map.bombMatrix[y][x].GetY()))
                bomb_map.RemoveBomb(x,y)
            else:
                screen.blit(bomb_map.bombMatrix[y][x].GetImage(),(bomb_map.bombMatrix[y][x].GetX(),bomb_map.bombMatrix[y][x].GetY()))

    for i in item_pos:
        item_pos[i].draw(screen)

    pressed_Key = pygame.key.get_pressed()

    blocks.PutsOnScreen(screen)
    
    #third argument pass how many time hada passed since last tiem
    p.Action(screen,pressed_Key,current_time, bomb_map)

    e.Action(screen, p, current_time)
    collectItem(p)

    #Reset current time
    current_time = 0.0

    pygame.display.update()



