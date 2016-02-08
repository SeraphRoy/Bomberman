import pygame
import random

item_pos = {}
grid = 51

class Item:
    def __init__(self,x,y,images):
        a = random.randint(1,4)
        if a == 1:
            item = Nike()
        if a == 2:
            item = Low_speed_field()
        if a == 3:
            item = Sadako()
        if a == 4:
            item = Heart()
        temp = pygame.image.load(images[a-1]).convert_alpha()
        item.image = pygame.transform.scale(temp,(grid,grid))
        item.x=x
        item.y=y
        item_pos[(x,y)]=item
        item.display=True

    def invoked(self, player):
        pass
  
    def draw(self,screen):
        if self.display:
            screen.blit(self.image,(self.x*grid,self.y*grid))


class Nike(Item):
    def __init__(self):
        pass
    def invoked(self,player):
        if player.speed > 0:
            player.speed += 50
        else:
            player.speed -=50


class Low_speed_field(Item):
    def __init__(self):
        pass
    def invoked(self,player):
        if player.speed > 0:
            player.speed -= 50
        else:
            player.speed += 50

class Sadako(Item):
    def __init__(self):
        pass
    def invoked(self, player):
        player.speed *= (-1)

class Heart(Item):
    def __init__(self):
        pass
    def invoked(self, player):
        player.GetDamge(-30)

def collectItem(player):
    x=(player.rect.x+player.image_x/2)//grid
    y=(player.rect.y+player.image_y/2)//grid
    if (x,y) in item_pos:
        item_pos[(x,y)].display=False
        item_pos[(x,y)].invoked(player)
        del item_pos[(x,y)]
