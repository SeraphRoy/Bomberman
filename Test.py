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
from Global import *
import random


pygame.init()


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



