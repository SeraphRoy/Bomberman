import pygame
from pygame.locals import *
from Img import *
from sys import *

OBJECT_X = 51
OBJECT_Y = 51
transparent = pygame.transform.scale(pygame.image.load(transparent_image),(OBJECT_X,OBJECT_Y))

class Object(pygame.sprite.Sprite):
    
    
    def __init__(self,isNull,objectType,image,x=500,y=600):
        pygame.sprite.Sprite.__init__(self)
        

        
        #self.time = 10000000
        self.isNull = isNull

        ''' Object Type
            0 = blank
            1 = Bomb
            2 = Block
            3 = Tofu
            4 = item
            5 = exploded bomb
            6 = transparent       
        '''
        self.type = objectType
        #self.x = x
        #self.y = y
        self.image = self.ConstructSurface(image)
        #self.nextImage = pygame.transform.scale(pygame.image.load(nextImage).convert_alpha(),(OBJECT_X,OBJECT_Y))
        self.x_Index = int(x//OBJECT_X)
        self.y_Index = int(y//OBJECT_Y)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_Index * OBJECT_X
        self.rect.y = self.y_Index * OBJECT_Y
        self.isVisible = True
        self.damageLength = 0

    def SetX(self,x):
        self.rect.x = x

    def SetY(self,y):
        self.rect.y = y

    def GetX(self):
        return self.rect.x
    
    def GetY(self):
        return self.rect.y

    def GetX_Index(self):
        return self.x_Index

    def GetY_Index(self):
        return self.y_Index

    def IsNull(self):
        return self.isNull
    
    def SetVisible(self,boolval):
        self.isVisible = boolval
        
    def SetDamageLength(self,damageLength):
        self.damageLength = damageLength
    
    def SetImage(self,image):
        self.image = image
    
    def ConstructSurface(self,image):
        return pygame.transform.scale(pygame.image.load(image).convert_alpha(),(OBJECT_X,OBJECT_Y))
        
    def Update(self):
        pass
    
    def Display(self, screen):
        if (self.isVisible == True):
            screen.blit(self.image, (self.rect.x, self.rect.y))
            
    def Explode(self):
        self.image = self.ConstructSurface(burst_image)
        self.type = 5
        
class ObjectMatrix:

    def __init__(self,X_MAX=15,Y_MAX=13):
        self.X_MAX = X_MAX
        self.Y_MAX = Y_MAX
        self.blank = Object(True,0,transparent_image)
        self.blank.SetVisible(False)
        self.objectMatrix = [[self.blank for x in range(X_MAX)] for y in range(Y_MAX)]
        self.all_bombs = pygame.sprite.Group()
        
    def Add(self,newObject):
        #print "Displayed at X = "
        #print newObject.GetX_Index()
        #print " y = " 
        #print newObject.GetY_Index()
        self.objectMatrix[newObject.GetY_Index()][newObject.GetX_Index()] = newObject
        #self.all_bombs.add(self.objectMatrix[newObject.GetX_Index()][newObject.GetY_Index()])
        

    def Update(self,screen,current_time):
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                if (self.objectMatrix[y][x].type != 0):
                    if (self.objectMatrix[y][x].type == 1):
                        if self.objectMatrix[y][x].TimePassed(current_time):
                            self.RemoveBomb(x,y,current_time)
                    else:
                        self.objectMatrix[y][x].Update()

        
    def Display(self,screen,current_time):
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                if (self.objectMatrix[y][x].type == 6):
                    print "666 x= ",x,"y= ",y
                    if self.objectMatrix[y][x].time-current_time<=0:
                        self.objectMatrix[y][x] = self.blank
                if (self.objectMatrix[y][x].type == 5):
                    print "5 to 6 x= ",x,"y= ",y
                    self.objectMatrix[y][x].time = 0.5
                    self.objectMatrix[y][x].type = 6
                    
                if (self.objectMatrix[y][x].isNull == False):
                    self.objectMatrix[y][x].Display(screen)



    def RemoveBomb(self,x_index,y_index,current_time):
        if self.objectMatrix[y_index][x_index].type == 5 or self.objectMatrix[y_index][x_index].type == 6:
            return
        xmax = x_index + self.objectMatrix[y_index][x_index].damageLength if (x_index + self.objectMatrix[y_index][x_index].damageLength < self.X_MAX) else X_MAX
        ymax = y_index + self.objectMatrix[y_index][x_index].damageLength if (y_index + self.objectMatrix[y_index][x_index].damageLength < self.Y_MAX) else Y_MAX
        xmin = x_index - self.objectMatrix[y_index][x_index].damageLength if (x_index - self.objectMatrix[y_index][x_index].damageLength >= 0) else 0
        ymin = y_index - self.objectMatrix[y_index][x_index].damageLength if (y_index - self.objectMatrix[y_index][x_index].damageLength >= 0) else 0
        self.objectMatrix[y_index][x_index].Explode()
        for x in range(x_index,xmin,-1):
            #self.Check(x,y_index)
            self.RemoveBomb(x,y_index,3)
        for y in range(y_index,ymin,-1):
            #self.Check(x_index,y)
            self.RemoveBomb(x_index,y,3)
        for x in range(x_index-1,xmax):
            #self.Check(x,y_index)
            self.RemoveBomb(x,y_index,3)
        for y in range(y_index-1,ymax):
            #self.Check(x_index,y)
            self.RemoveBomb(x_index,y,3)
            
    def Check(self,x,y):
        if self.objectMatrix[y][x].type == 2:
            return
        if self.objectMatrix[y][x].type == 1:
            #if self.objectMatrix[y][x].TimePassed(current_time):
            self.RemoveBomb(x,y,3)
            print "x= ",x,"y= ",y 
                    
    
'''
    def RemoveBomb(self,screen, x_Index, y_Index,burst, player, damage, all_enemies):
        explode = Explode(burst, y_Index, x_Index, self.bombMatrix[y_Index][x_Index].GetDamageLength())
        all_explodes = pygame.sprite.Group()
        all_explodes.add(explode)
        for i in range(1, self.bombMatrix[y_Index][x_Index].GetDamageLength()):
            explode1 = Explode(burst, y_Index+i, x_Index, self.bombMatrix[y_Index][x_Index].GetDamageLength())
            explode2 = Explode(burst, y_Index-i, x_Index, self.bombMatrix[y_Index][x_Index].GetDamageLength())
            explode3 = Explode(burst, y_Index, x_Index+i, self.bombMatrix[y_Index][x_Index].GetDamageLength())
            explode4 = Explode(burst, y_Index, x_Index-i, self.bombMatrix[y_Index][x_Index].GetDamageLength())
            all_explodes.add(explode1)
            all_explodes.add(explode2)
            all_explodes.add(explode3)
            all_explodes.add(explode4)
        for explodes in all_explodes:
            screen.blit(burst, (explodes.GetX(), explodes.GetY()))
        if pygame.sprite.spritecollide(player, all_explodes, False, pygame.sprite.collide_rect_ratio(0.6)):
            player.GetDamge(damage)
        deadDic = pygame.sprite.groupcollide(all_enemies, all_explodes, True, True, pygame.sprite.collide_rect_ratio(0.6))
        for e in deadDic:
            e.GetDamage(10)
            if e.CheckAlive() == True:
                all_enemies.add(e)


        #screen.blit(burst,(self.bombMatrix[y_Index][x_Index].GetX(),self.bombMatrix[y_Index][x_Index].GetY()))
        self.bombMatrix[y_Index][x_Index] = self.null_Bomb
        self.all_bombs.remove(self.bombMatrix[y_Index][x_Index])
        # affected_bombs = pygame.sprite.groupcollide(self.all_bombs, all_explodes, False, False, pygame.sprite.collide_rect_ratio(0.8))
        # for b in affected_bombs:
        #     if b.GetX_Index() != x_Index and b.GetY_Index() != y_Index:
        #         self.RemoveBomb(screen, b.GetX_Index(), b.GetY_Index(), burst, player, damage, all_enemies)
        
        dmg = self.bombMatrix[y_Index][x_Index].GetDamageLength()
        if (x_Index >= 1) and (self.bombMatrix[y_Index][x_Index-1].IsNull() == False):
            self.RemoveBomb(screen,x_Index-1,y_Index,burst, player, damage, all_enemies)
        if (y_Index >= 1) and (self.bombMatrix[y_Index-1][x_Index].IsNull() == False):
            self.RemoveBomb(screen,x_Index,y_Index-1,burst, player, damage, all_enemies)
        if (x_Index <= self.x_MAX-2) and (self.bombMatrix[y_Index][x_Index+1].IsNull() == False):
            self.RemoveBomb(screen,x_Index+1,y_Index,burst, player, damage, all_enemies)
        if (y_Index <= self.y_MAX-2) and (self.bombMatrix[y_Index+1][x_Index].IsNull() == False):
            self.RemoveBomb(screen,x_Index,y_Index+1,burst, player, damage, all_enemies)
        
    def CheckAllBombs(self, screen, current_time, X_INDEX, Y_INDEX,burst, player, damage, all_enemies):
        for x in range(X_INDEX):
            for y in range(Y_INDEX):
                if (self.bombMatrix[y][x].isNull == False) and (self.bombMatrix[y][x].TimePassed(current_time) == True):
                    self.RemoveBomb(screen,x,y,burst, player, damage, all_enemies)
                else:
                   screen.blit(self.bombMatrix[y][x].GetImage(),(self.bombMatrix[y][x].GetX(),self.bombMatrix[y][x].GetY()))

class Explode(pygame.sprite.Sprite):

    def __init__(self, image, x_index, y_index, damageLength):
        pygame.sprite.Sprite.__init__(self)
        #temp = pygame.image.load(image).convert_alpha()
        #self.image = pygame.transform.scale(image,(bomb.BOMB_IMG_X, bomb.BOMB_IMG_Y))
        BOMB_IMG_X = 51
        BOMB_IMG_Y = 51
        self.image = image
        self.rect = self.image.get_rect()
        self.dmgLength = damageLength
        self.x_index = x_index
        self.y_index = y_index
        self.img_x = self.x_index * BOMB_IMG_X
        self.img_y = self.y_index * BOMB_IMG_Y
        self.rect.x = self.img_x
        self.rect.y = self.img_y
        '''