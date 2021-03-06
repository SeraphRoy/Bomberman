import pygame
from pygame.locals import *

#function to change Enemy's image index
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



class Enemy(pygame.sprite.Sprite):
		#Enemy's image size
		image_x = 51
		image_y = 51 
		#background size
		map_x = 768
		map_y = 666

		def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
                        pygame.sprite.Sprite.__init__(self)

			if len(imagenames)!=16:
				print("Number of images is wrong")

			self.images = []

			for name in imagenames:
				temp = pygame.image.load(name).convert_alpha()
				temp = pygame.transform.scale(temp, (self.image_x,self.image_y))
				self.images.append(temp)

			self.speed = speed
			#enemy will switch to rushing speed when certain requirment is fullfilled
			self.rushingSpeed = rushingSpeed

			self.rushing = False
                        self.rect = self.images[0].get_rect()
			self.rect.x = x
			self.rect.y = y
			self.time = 0.5
			self.timeChange = 0.5
			self.radary = radary
			self.radarx = radarx
			self.warning = False
			#0 = left, 1 = right, 2 = up, 3 = down
			self.lastcommand = 0
			self.image_index = 5
			self.timetochange = 4
			self.changeedDirection = False

                        self.hp = 1
			#for patrol
			self.down = True
			self.up = False

			#damge when touch the player
			self.damage = 20
                        self.isAlive = True

                def LiveAction():
                        print("it is origin's action, you should not call this function")
                                
        #it is origin's action, you should not call this function        
		def Action(self, screen, player, seconds):
			print("it is origin's action, you should not call this function")

                def SetAlive(self, value):
                        self.isAlive = value
                        
                def GetDamage(self, value):
                        self.hp -= value
                        if self.hp <= 0:
                                self.hp = 0
                                self.isAlive = False

                def CheckAlive(self):
                        return self.isAlive
