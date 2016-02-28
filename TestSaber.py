from Player1 import Player
from Img import *
import pygame
from pygame.locals import *
from sys import exit
from Block1 import *
from Object import *
from Bomb1 import *
from Global import *
from Tofu import *
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1024,768),0,32)

background = pygame.image.load(back_ground_name).convert()
bomb = pygame.image.load(bomb_image).convert_alpha()
bomb = pygame.transform.scale(bomb, (32,32))
burst = pygame.image.load(burst_image).convert_alpha()
burst = pygame.transform.scale(burst,(64,59))

'''
player_images = [player_up1,player_up2,player_up3,player_up4,
                 player_down1,player_down2,player_down3,player_down4,
                 player_left1,player_left2,player_left3,player_left2,
                 player_right1,player_right2,player_right3,player_right4]
'''
p = Player(player_images,bomb_image,150,10,20,9,1,hp_image)

#setOfBlocks = [(100,100), (52,52), (240,240), (49, 203), (500, 20)]
#blocks = Block(block_image, setOfBlocks)

object_map = ObjectMatrix(X_INDEX,Y_INDEX)

#display blocks
setOfBlocks = [(2,2), (3,4), (3, 5), (3, 6), (3, 7)]
all_objects = pygame.sprite.Group()
for point in setOfBlocks:
   block = Block(block_image, point[0], point[1])
   all_objects.add(block)
   object_map.Add(block)

setOfTofu = [(4,5),(7,6),(12,5),(6,14)]
for point in setOfBlocks:
   tofu = Tofu(block_image, point[0], point[1])
   all_objects.add(tofu)
   object_map.Add(tofu)
   

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

    for everyObject in all_objects:
        everyObject.Display(screen)
    
    object_map.Display(screen)
    object_map.Update(screen,current_time)
    
    pressed_Key = pygame.key.get_pressed()

    #blocks.PutsOnScreen(screen)
    
    #third argument pass how much time passed since last tiem
    p.Action(screen,pressed_Key,current_time, object_map,hp_image)

    #Reset current time
    current_time = 0.0

    pygame.display.update()


print "import success"
