back_ground_name = 'Background02.jpg'
player_image = 'down1.png'
player_image_right = 'right2.png'
player_image_up = 'up2.png'
player_image_left = 'left2.png'
player_image_down = 'down4.png'
bomb_image = 'bomb.png'
burst_iamge = 'burst.png'

import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((1024,698),0,32)

background = pygame.image.load(back_ground_name).convert()
player = pygame.image.load(player_image).convert_alpha()
player = pygame.transform.scale(player, (42,73))
bomb = pygame.image.load(bomb_image).convert_alpha()
bomb = pygame.transform.scale(bomb, (32,32))
burst = pygame.image.load(burst_iamge).convert_alpha()
burst = pygame.transform.scale(burst,(64,59))

x = 0
y = 10
bomb_x = 0
bomb_y = 10
bomb_placed = False
count_down = 300
burst_happened = False
burst_x = 0
burst_y = 10
burst_count_down = 100

speed = 5

clock = pygame.time.Clock()

while True:    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    screen.blit(background, (0,0))
    if(bomb_placed):
        screen.blit(bomb,(bomb_x,bomb_y))
    if(burst_happened):
        screen.blit(burst,(burst_x,burst_y))

    screen.blit(player, (x,y))

    pressed_Key = pygame.key.get_pressed()

    if pressed_Key[K_LEFT]:
        if((x-speed)<0):
            x=0
        else:
            x-=speed
        player = pygame.image.load(player_image_left).convert_alpha()
    elif pressed_Key[K_RIGHT]:
        if ((x+speed)>980):
            x = 980
        else:
            x+=speed
        player = pygame.image.load(player_image_right).convert_alpha()
    elif pressed_Key[K_UP]:
        if ((y-speed<0)):
            y = 0
        else:
            y-=speed
        player = pygame.image.load(player_image_up).convert_alpha()
    elif pressed_Key[K_DOWN]:
        if ((y+speed)>630):
            y = 630
        else:
            y+=speed
        player = pygame.image.load(player_image_down).convert_alpha()
    elif pressed_Key[K_SPACE]:
        if(bomb_placed==False):
            count_down=300
            bomb_placed = True
            bomb_x = x+12
            bomb_y = y+35
    else:
        player = pygame.image.load(player_image).convert_alpha()

    if(bomb_placed):
        count_down-=1

    if(burst_happened):
        burst_count_down-=1

    if(burst_count_down<=0):
        burst_count_down=100
        burst_happened=False

    if(count_down<=0):
        count_down=500
        bomb_placed=False
        burst_happened = True
        burst_x = bomb_x
        burst_y = bomb_y
        
    player = pygame.transform.scale(player, (42,73))
    pygame.display.update()
