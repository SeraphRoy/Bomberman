from Player import Player
from Img import *
import pygame
from pygame.locals import *
from sys import exit
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((768,768),0,32)

background = pygame.image.load(back_ground_name).convert()
bomb = pygame.image.load(bomb_image).convert_alpha()
bomb = pygame.transform.scale(bomb, (32,32))
burst = pygame.image.load(burst_iamge).convert_alpha()
burst = pygame.transform.scale(burst,(64,59))


player_images = [player_up1,player_up2,player_up3,player_up4,
                 player_down1,player_down2,player_down3,player_down4,
                 player_left1,player_left2,player_left3,player_left2,
                 player_right1,player_right2,player_right3,player_right4]

p = Player(player_images,bomb_image,150,10,20,1,1)

bomb_queue = []
total_time = 0.05
current_time = 0.0
exploded_queue = []

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

    for b in bomb_queue:
        if b.TimePassed(current_time) == True :
            screen.blit(burst,(b.GetX(),b.GetY()))
            bomb_queue.remove(b)
        else:
            screen.blit(b.GetImage(),(b.GetX(),b.GetY()))


    pressed_Key = pygame.key.get_pressed()

    #third argument pass how many time hada passed since last tiem
    p.Action(screen,pressed_Key,current_time, bomb_queue)

    #Reset current time
    current_time = 0.0

    pygame.display.update()


print "import success"
