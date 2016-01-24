import pygame
from pygame.locals import *
from Bomb import *

#1->left is pressed, 2->up, 3->right, 4->down
def ChangeNextIndex(current, key):
    if current<0 or current>15:
        print "incorrect current image index"
        return
    if key == 1:
        if current>7 and current<12:
            if current == 11:
                return 8
            else:
                return current+1
            
        else:
             return 9
    

    elif key == 2:
        if current<4:
            if current == 3:
                return 0
            else:
                return current+1
        else:
            return 1


    elif key==3:
        if current>11 and current<16:
            if current == 15:
                return 12
            else:
                return current+1
        else:
            return 13

    elif key == 4:
        if current<8 and current>3:
            if current ==7:
                return 4
            else:
                return current+1
        else:
            return 5
        
        

class Player:
    image_x = 42
    image_y = 73
    background_x = 600
    background_y = 700
    #image in the order of up, down, left, right
    def __init__(self, image_names, bomb_name,speed,x,y, max_bomb, bomb_damage):
        if(len(image_names)!=16):
            print "incorrect size of the iamge_names\n"
        
        self.images = []
        for names in image_names:
            temp = pygame.image.load(names).convert_alpha()
            temp = pygame.transform.scale(temp, (temp.get_width(),
                                                 temp.get_height()))
            self.images.append(temp)
        
        self.bomb_name = bomb_name

        self.speed = speed
        self.x = x;
        self.y =y;
        self.max_bomb = max_bomb
        self.bomb_damage = bomb_damage
        self.current_image = self.images[4]
        self.image_index = 4
        self.time = 0

        #used to restirct putting too many bomb at a moment
        self.bomb_since_last = 0


    def Action(self, screen, pressed_Key,seconds, bomb_map):
        background_x = 740
        background_y = 630
        self.time+=seconds
        self.bomb_since_last+=seconds
        switch = False
        if self.time >= 0.2:
            switch = True
            self.time = 0

        distance = seconds * self.speed

        if pressed_Key[K_SPACE] and self.bomb_since_last>=0.5:
            self.bomb_since_last = 0
            new_bomb = Bomb(self.bomb_name,int(self.x+25),int(self.y+25))
            bomb_map.AddBomb(new_bomb)
        if (pressed_Key[K_LEFT]) and (self.x >= 15):
            self.x-=distance
            if switch == True or self.image_index<8 or self.image_index>11:
                self.image_index = ChangeNextIndex(self.image_index,1)
        elif (pressed_Key[K_RIGHT])and(self.x <= background_x-25):
            self.x+=distance
            if switch == True or self.image_index<12:
                self.image_index = ChangeNextIndex(self.image_index,3)
        elif (pressed_Key[K_UP])and(self.y >= 15):
            self.y-=distance
            if switch == True or self.image_index>3:
                self.image_index =ChangeNextIndex(self.image_index,2)
        elif (pressed_Key[K_DOWN])and(self.y <= background_y-25):
            self.y+=distance
            if switch == True or self.image_index<4 or self.image_index>7:
                self.image_index = ChangeNextIndex(self.image_index,4)
        else:
            self.image_index = (self.image_index/4)*4
        screen.blit(self.images[self.image_index],(self.x,self.y))
    
