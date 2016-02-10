import pygame
import random

item_pos = {}
grid = 51

class ToolBar:
    GRID = 65
    def __init__(self):
        self.dict = {}
    def register(self, tool):
        if tool.name() in self.dict:
            self.dict[tool.name()].append(tool)
        else:
            self.dict[tool.name()] = [tool]
    def draw(self, screen):
        x = 260
        y = 680
        for i in self.dict:
            item = self.dict[i][0]
            image = pygame.transform.scale(item.image, (self.GRID, self.GRID))
            screen.blit(image, (x,y))
            x += self.GRID
        #print(self.dict)
            
toolbar = ToolBar()

class Item:
    pos = {}
    def __init__(self,x,y,images):
        a = random.randint(1,7)
        if a == 1:
            item = Nike()
        if a == 2:
            item = Low_speed_field()
        if a == 3:
            item = Sadako()
        if a == 4:
            item = Heart()
        if a == 5:
            item = Tool1()
        if a == 6:
            item = Tool2()
        if a == 7:
            item = Stimpack()
        temp = pygame.image.load(images[a-1]).convert_alpha()
        item.image = pygame.transform.scale(temp,(grid,grid))
        item.x=x
        item.y=y
        Item.pos[(x,y)]=item
        item.display=True

    def invoked(self, player):
        pass
  
    def draw(self,screen):
        if self.display:
            screen.blit(self.image,(self.x*grid,self.y*grid))

class Tool(Item):
    def __init__(self):
        pass
    def invoked(self, player):
        toolbar.register(self)
    def name(self):
        return self.__class__.__name__

class Nike(Tool):
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)
        if player.speed > 0:
            player.speed += 50
        else:
            player.speed -=50

class Tool1(Tool):
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)

class Tool2(Tool):
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)


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

class Stimpack(Item):
    def __init__(self):
        pass
    def invoked(self,player):
        player.bomb_damage += 1
            
def collectItem(player):
    x=(player.rect.x+player.image_x/2)//grid
    y=(player.rect.y+player.image_y/2)//grid
    if (x,y) in Item.pos:
        Item.pos[(x,y)].display=False
        Item.pos[(x,y)].invoked(player)
        del Item.pos[(x,y)]
