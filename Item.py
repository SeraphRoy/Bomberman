import pygame
import random

grid = 51

class ToolBar:
    GRID = 65
    def __init__(self):
        self.dict = {}
    def register(self, tool):   ## put tools into toolbar after collecting them
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
            
toolbar = ToolBar()

class Item:
    pos = {}    ## a dictionary with position as keys and items as values
    def __init__(self,x,y,images):
        a = random.randint(1,7)     ## randomly generate an item
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

    def invoked(self, player):      ## the effects on player after being collected
        pass
  
    def draw(self,screen):
        if self.display:
            screen.blit(self.image,(self.x*grid,self.y*grid))

class Tool(Item):       ## the kind of items that can be stored in toolbar
    def __init__(self):
        pass
    def invoked(self, player):
        toolbar.register(self)
    def name(self):
        return self.__class__.__name__

class Nike(Tool):       ## increases player's speed
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)
        if player.speed > 0:
            player.speed += 50
        else:
            player.speed -=50

class Tool1(Tool):      ## for testing, does nothing
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)

class Tool2(Tool):      ## for testing, does nothing
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)


class Low_speed_field(Item):        ## decreases player's speed
    def __init__(self):
        pass
    def invoked(self,player):
        if player.speed > 0:
            player.speed -= 50
        else:
            player.speed += 50

class Sadako(Item):     ## reverts key input, player goes opposite directions
    def __init__(self):
        pass
    def invoked(self, player):
        player.speed *= (-1)

class Heart(Item):      ## recovers player's HP
    def __init__(self):
        pass
    def invoked(self, player):
        player.GetDamge(-30)

class Stimpack(Item):       ## adds damage of bombs player places
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
