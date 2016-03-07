import pygame
import random

grid = 51

class ToolBar:
    GRID = 65
    def __init__(self):
        self.dict = {}      ## key: name of tool; value: list of tools of the name
        self.li = []        ## list of names of tools in the toolbar
        
    def register(self, tool):   ## put tools into toolbar after collecting them
        if tool.name() in self.dict:
            self.dict[tool.name()][0] += 1
        else:
            self.dict[tool.name()] = [1]
            for i in range(len(self.li)):
                if self.li[i] == 0:
                    self.li[i] = tool.name()
                    break
            else:
                self.li.append(tool.name())
        self.dict[tool.name()].append(tool)
        print self.dict
        print self.li
        
    def use(self, player, index):
        if (index >= len(self.li)) or (self.li[index] == 0):
            return
        name = self.li[index]
        self.dict[name].pop().used(player)
        self.dict[name][0] -= 1
        if self.dict[name][0] == 0:
            del self.dict[name]
            self.li[index] = 0
        print self.dict
        print self.li
            
    def draw(self, screen):
        x = 260
        y = 680
        for i in range(len(self.li)):
            if self.li[i] != 0:
                item = self.dict[self.li[i]][1]
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
            item = Blood()
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
    def used(self, player):
        pass
    def name(self):
        return self.__class__.__name__

class Nike(Item):       ## increases player's speed
    def __init__(self):
        pass
    def invoked(self,player):
        if player.slowed:
            player.speed = player.initial_speed
            player.slowed = False
        else:
            if player.speed > 0:
                player.speed += 50
                if player.speed > 250:
                    player.speed = 250
            else:
                player.speed -=50
                if player.speed < -250:
                    player.speed = -250

class Blood(Tool):      ## recovers player's HP when he chooses to do so
    def __init__(self):
        pass
    def used(self,player):
        player.GetDamge(-30)

class Tool2(Tool):      ## for testing, does nothing
    def __init__(self):
        pass
    def invoked(self,player):
        Tool.invoked(self, player)


class Low_speed_field(Item):        ## decreases player's speed
    def __init__(self):
        pass
    def invoked(self,player):
        if not (player.slowed):
            player.initial_speed = player.speed
            if player.speed > 0:
                player.speed -= 50
            else:
                player.speed += 50
            player.slowed = True
        player.slow_time = 10

class Sadako(Item):     ## reverts key input, player goes opposite directions
    def __init__(self):
        pass
    def invoked(self, player):
        if player.inversed:
            player.inversed = False
            player.inverse_time = 0
        else:
            player.inversed = True
            player.inverse_time = 10
        player.speed *= (-1)
        player.initial_speed *= (-1)

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

def randomItem(number, images):     ## construct number of random items
    for i in range(number):
        item_x = random.randint(0,14)
        item_y = random.randint(0,12)
        Item(item_x,item_y,images)
