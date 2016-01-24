import pygame
import random

item_pos={}

class Item:
    def __init__(self,x,y,images):
        a=random.randint(1,3)
        if a==1:
            item=Nike()
            item.image=pygame.image.load(images[0]).convert()
        if a==2:
            item=Low_speed_field()
            item.image=pygame.image.load(images[1]).convert()
        if a==3:
            item=Sadako()
            item.image=pygame.image.load(images[2]).convert()
        item.x=x
        item.y=y
        item_pos[(x,y)]=item
        item.display=True

    
    def draw(self,screen):
        if self.display:
            screen.blit(self.image,(self.x*50,self.y*50))


class Nike(Item):
    def __init__(self):
        pass
    def invoked(self,player):
        player.speed += 50


class Low_speed_field(Item):
    def __init__(self):
        pass
    def invoked(self,player):
        player.speed -= 50

class Sadako(Item):
    def __init__(self):
        pass
    def invoked(self, player):
        #player.speed *= (-1) <- will go out of the screen
        pass

def collectItem(player):
    x=(player.x+player.image_x/2)//50
    y=(player.y+player.image_y/2)//50
    if (x,y) in item_pos:
        item_pos[(x,y)].display=False
        item_pos[(x,y)].invoked(player)
        del item_pos[(x,y)]

