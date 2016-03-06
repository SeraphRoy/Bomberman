import pygame
from pygame.locals import *
from Img import transparent_image
from sys import *
class Bomb(pygame.sprite.Sprite):
 

    def __init__(self,image, x = -50, y = -50,damageLength = 2, isNull = False):
        pygame.sprite.Sprite.__init__(self)
        BOMB_IMG_X = 51
        BOMB_IMG_Y = 51
        temp = pygame.image.load(image).convert_alpha()
        self.damageLength = damageLength
        self.image = pygame.transform.scale(temp,(BOMB_IMG_X,BOMB_IMG_Y))
        self.time = 2.0
        self.rect = self.image.get_rect()
        self.x_Index = int(x//BOMB_IMG_X)
        self.rect.x = self.x_Index * BOMB_IMG_X
        self.y_Index = int(y//BOMB_IMG_Y)
        self.rect.y = self.y_Index * BOMB_IMG_Y
        self.isNull = isNull

    #check if time is over
    def TimePassed(self,t):
        self.time-=t
        if self.time<=0:
            return True
        else:
            return False

    def GetImage(self):
        return self.image

    def SetX(self,x):
        self.rect.x = x

    def SetY(self,y):
        self.rect.y = y

    def SetDamageLength(self,damageLength):
        self.damageLength = damageLength

    # Call this method when player recieved an increase-bomb-power item
    def IncrDamageLength(self):
        self.damageLength += 1

    def GetDamageLength(self):
        return self.damageLength

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



class BombMatrix:

    def __init__(self,X_MAX=13,Y_MAX=15):
        self.x_MAX = X_MAX
        self.y_MAX = Y_MAX
        self.null_Bomb = Bomb(transparent_image,-50,-50,0,True)
        self.bombMatrix = [[self.null_Bomb for x in range(X_MAX)] for y in range(Y_MAX)]
        self.all_bombs = pygame.sprite.Group()

    #add bomb into the bomb matrix
    def AddBomb(self, newBomb):
        self.bombMatrix[newBomb.GetX_Index()][newBomb.GetY_Index()] = newBomb
        self.all_bombs.add(self.bombMatrix[newBomb.GetX_Index()][newBomb.GetY_Index()])

    #remove bomb from the matrix and explode
    def RemoveBomb(self,screen, x_Index, y_Index,burst, player, damage, all_enemies):
        explode = Explode(burst, y_Index, x_Index, self.bombMatrix[y_Index][x_Index].GetDamageLength())
        all_explodes = pygame.sprite.Group()
        all_explodes.add(explode)
        explode_sound = pygame.mixer.Sound("music/explode.wav")
        explode_sound.play()
        explode_sound.set_volume(0.4)
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
            all_enemies.remove(e)
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

    #check all the bombs to see if they need to explode
    def CheckAllBombs(self, screen, current_time, X_INDEX, Y_INDEX,burst, player, damage, all_enemies):
        for x in range(X_INDEX):
            for y in range(Y_INDEX):
                if (self.bombMatrix[y][x].isNull == False) and (self.bombMatrix[y][x].TimePassed(current_time) == True):
                    self.RemoveBomb(screen,x,y,burst, player, damage, all_enemies)
                else:
                   screen.blit(self.bombMatrix[y][x].GetImage(),(self.bombMatrix[y][x].GetX(),self.bombMatrix[y][x].GetY()))


#class for explode and damage for bombs
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


    def GetXIndex(self):
        return self.x_index

    def GetYIndex(self):
        return self.y_index

    def GetX(self):
        return self.img_x

    def GetY(self):
        return self.img_y
