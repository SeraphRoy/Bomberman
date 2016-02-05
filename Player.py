import pygame
import math
from pygame.locals import *
from Bomb import *
from Block import *

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
	background_x = 720
	background_y = 615
	#image in the order of up, down, left, right
	def __init__(self, image_names, bomb_name,speed,x,y, max_bomb, bomb_damage, hp_image):
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
		self.HP = 100
		self.hurt_turn = 0;
		#when show =0, program will not display player's image, flashing
		self.show = 1;

		#used to restirct putting too many bomb at a moment
		self.bomb_since_last = 0

		#knock turn, indicate how many turns the player will be knock back
		self.knock = 0
		self.knockDirection = 0
		self.knockspeed = 450
		self.hp_image = pygame.image.load(hp_image).convert_alpha()
		self.hp_image = pygame.transform.scale(self.hp_image, (self.image_x-4,10))
		self.alive = True

		#image replace at right down corner when hurted
		self.hurt_face = pygame.image.load('img/hurt_face.png').convert()

		self.invincible_turn = 0

	def CheckAlive(self):
		return self.alive

	def GetX(self):
		return self.x

	def GetY(self):
		return self.y

	def GetInvincible(self):
		return self.invincible_turn

	def GetDamge(self, damage):
		#turn to invincible
		self.invincible_turn = 15;
		if(self.HP-damage<=0):
			self.hp = 0
			self.alive = False
		else:
			self.HP-=damage
		self.hurt_turn = 10;
		new_width = (self.HP / 100.0) * (self.image_x-4)
		self.hp_image = pygame.transform.scale(self.hp_image, (int(new_width),10))


	def KnockBack(self,direction):
		self.knock = 3
		self.knockDirection = direction

	def Action(self, screen, pressed_Key,seconds, bomb_map, block):
		#check if player is invincible 
		if self.invincible_turn>0:
			#flashing affect
			if(self.show==1):
				self.show = 0
			else:
				self.show = 1
			self.invincible_turn-=1

		#count down for the time that hurt_face will display
		if(self.hurt_turn>0):
			self.hurt_turn-=1
			screen.blit(self.hurt_face, (665, 665))

		#check if player is currently being knock
		if self.knock>0:
			#decrease the turn
			self.knock-=1
			distance = self.knockspeed * seconds

			#check knock direction
			if self.knockDirection == 1:
				if self.x - distance >0:
					self.x-=distance
				else:
					self.x = 0
			elif self.knockDirection == 3:
				if self.x + distance <self.background_x:
					self.x+=distance
				else:
					self.x = self.image_x
			elif self.knockDirection == 2:
				if self.y - distance>0:
					self.y-=distance
				else:
					self.y = 0
			elif self.knockDirection == 4:
				if self.y+distance<self.background_y:
					self.y+=distance
				else:
					self.y = self.background_y
			screen.blit(self.images[self.image_index],(self.x,self.y))
			return;

		self.time+=seconds
		self.bomb_since_last+=seconds
		switch = False

		#check if it is time to change the image index 
		if self.time >= 0.2:
			switch = True
			self.time = 0

		distance = seconds * self.speed

		if pressed_Key[K_SPACE] and self.bomb_since_last>=0.2:
			self.bomb_since_last = 0

			# Becareful with this line, need to check index out of bound exception
			new_bomb = Bomb(self.bomb_name,int(self.x+23),int(self.y+23))

			bomb_map.AddBomb(new_bomb)
			#print (self.x)
			#print (",")
			#print (self.y)

		# 1 = left, 2 = up, 3 = right, 4 = down
		if pressed_Key[K_LEFT]:
			self.x-=distance
                        for point in block.GetSet():
                                if self.x + distance >= point[0] + block.image_x*2/3 and self.x - point[0] - block.image_x*3/4 <= 0 and self.y - point[1] <= block.image_y*2/3 and point[1] - self.image_y*2/3 - self.y <= 0:
                                        self.x += distance
                                        break
			if self.x < 0:
				self.x = 0
			#if self.x > self.background_x:
			#	self.x = self.background_x
			
			#only change the image when switch is true
			if switch == True or self.image_index<8 or self.image_index>11:
				self.image_index = ChangeNextIndex(self.image_index,1)
		elif pressed_Key[K_RIGHT]:
			self.x+=distance
                        for point in block.GetSet():
                                if self.x - distance <= point[0] and point[0] - self.x - self.image_x*3/5 <= 0 and self.y - point[1] <= block.image_y*2/3 and point[1] - self.image_y*2/3 - self.y <= 0:
                                        self.x -= distance
                                        break
			#if self.x < 0:
			#	self.x = 0
			if self.x > self.background_x:
				self.x = self.background_x
			if switch == True or self.image_index<12:
				self.image_index = ChangeNextIndex(self.image_index,3)
		elif pressed_Key[K_UP]:
			self.y-=distance
                        for point in block.GetSet():
                                if self.y + distance >= point[1] + block.image_y*2/3 and self.y - point[1] - block.image_y*3/5 <= 0 and self.x - point[0] - block.image_x*3/5 <= 0 and point[0] - self.image_x*3/5 - self.x <= 0:
                                        self.y += distance
                                        break
			if self.y < 0:
				self.y = 0
			#If self.y > self.background_y:
			#	self.y = self.background_y
			if switch == True or self.image_index>3:
				self.image_index =ChangeNextIndex(self.image_index,2)
		elif pressed_Key[K_DOWN]:
			self.y+=distance
                        for point in block.GetSet():
                                if self.y - distance <= point[1] and point[0] - self.y - self.image_y*3/5 <= 0 and self.x - point[0] - block.image_x*3/5 <= 0 and point[0] - self.image_x*3/5 - self.x <= 0:
                                        self.y -= distance
                                        break
			#if self.y < 0:
	                #    self.y = 0
			if self.y > self.background_y:
				self.y = self.background_y
			if switch == True or self.image_index<4 or self.image_index>7:
				self.image_index = ChangeNextIndex(self.image_index,4)
		else:
			self.image_index = (self.image_index/4)*4
		if self.invincible_turn<=0 or self.show == 1: 
			screen.blit(self.hp_image,(self.x,self.y-13))
			screen.blit(self.images[self.image_index],(self.x-5,self.y))
	
