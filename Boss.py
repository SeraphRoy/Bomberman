from Enemy import *
from Global import *
from Bomb import Bomb

flame_image_names = [flame01,flame02,flame03,flame04,flame05,
					 flame06,flame07,flame08,flame09,flame10,
					 flame11,flame12,flame13,flame14,flame15,
					 flame16,flame17,flame18]

class Boss(Enemy):
	def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
		Enemy.__init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary)
		self.hp = 100
		#throwing bomb in random position
		self.bomb_each_time = 4
		self.bomb_damge = 5
		self.bomb_countdown = 20
		self.throwing = 0
		self.bomb_x_array = []
		self.bomb_y_array = []
		#bomb's current location (animation phase) 
		self.current_bomb_x_array = []
		self.current_bomb_y_array = []

		#flame damage
		self.flameImages = []
		for name in flame_image_names:
			temp = pygame.image.load(name).convert_alpha()
			self.flameImages.append(temp)

        def LiveAction(self, screen, player, seconds, bomb_map):
                if self.isAlive:
                        self.Action(screen, player, seconds, bomb_map)
                        
	def Action(self, screen, player, seconds,bomb_map):
		xDistance = player.GetX()-self.rect.x
		#distance in y direction between player and enemy
		yDistance = player.GetY()-self.rect.y

		distance =0;
		self.time+=seconds

		#use in later throwing phase, place holder
		current_x = 0
		current_y = 0
		dest_x = 0
		dest_y = 0
		change =0


		if self.bomb_countdown>0:
			self.bomb_countdown-=1;
		else:
			self.bomb_x_array = []
			self.bomb_y_array = []
			self.current_bomb_x_array = []
			self.current_bomb_y_array = []
			self.bomb_countdown = 200
			self.throwing = 20

			for i in range(self.bomb_each_time):
				self.bomb_x_array.append(random.randint(0,12))
				self.bomb_y_array.append(random.randint(0,12))
				self.current_bomb_x_array.append(self.rect.x)
				self.current_bomb_y_array.append(self.rect.y)

		if self.throwing>0:
			for i in range(self.bomb_each_time):
				current_x = self.current_bomb_x_array[i]
				dest_x = self.bomb_x_array[i]*51
				change = (int)((dest_x-current_x)/self.throwing)
				self.current_bomb_x_array[i]+=change

				current_y = self.current_bomb_y_array[i]
				dest_y = self.bomb_y_array[i]*51
				change = (int)((dest_y - current_y)/self.throwing)
				self.current_bomb_y_array[i]+=change

			self.throwing-=1

		elif len(self.bomb_x_array) != 0:
			for i in range(self.bomb_each_time):
				new_bomb = Bomb(bomb_image,self.bomb_x_array[i]*51,self.bomb_y_array[i]*51,4)
				bomb_map.AddBomb(new_bomb)
		else:
			self.bomb_x_array = []
			self.bomb_y_array = []
			self.current_bomb_x_array = []
			self.current_bomb_y_array = []




		if self.timetochange>0:
			self.timetochange-=1
		else:
			self.timetochange = 4

		distance = seconds * self.speed

		if abs(xDistance)>self.speed/2 or abs(yDistance)>self.speed/2:
			if self.time<self.timeChange:
				#if it is time to change the direction
				if self.timetochange==0:
					self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
				if self.lastcommand == 1 and (self.rect.x- distance)>0:
					self.rect.x-=distance
				elif self.lastcommand == 3 and (self.rect.x + distance)<self.map_x:
					self.rect.x+=distance
				elif self.lastcommand == 2 and (self.rect.y - distance)>0:
					self.rect.y-=distance
				elif (self.rect.y+distance)<self.map_y:
					self.rect.y+=distance
			else:
				self.time = 0;
				#when player is farer away in X direction then y direction, move to x direction
				if (abs(xDistance)-abs(yDistance))>self.speed/4:
					if xDistance>distance:
						if (self.rect.x + distance)<self.map_x:
							self.rect.x+=distance
						else:
							self.rect.x = self.map_x
						self.lastcommand = 3
					elif xDistance<distance :
						if (self.rect.x- distance)>0:
							self.rect.x-=distance
						else:
							self.rect.x = 0
						self.lastcommand = 1
					self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)	
				#move in y direction
				else:
					if yDistance>distance:
						if (self.rect.x- distance)>0:
							self.rect.y+=distance
						else:
							self.rect.y = self.map_y
						self.lastcommand = 4
					elif yDistance<distance:
						if (self.rect.y - distance)>0:
							self.rect.y-=distance
						else:
							self.rect.y = 0
						self.lastcommand = 2
					self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
		#player is hitted by ghost, check if player is currently invincible
		elif player.GetInvincible()<=0:
			player.GetDamge(self.damage)
			player.KnockBack(self.lastcommand)



		screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y))
		if(self.throwing>0):
			for i in range(self.bomb_each_time):
				screen.blit(bomb, (self.current_bomb_x_array[i], self.current_bomb_y_array[i]))

        def GetDamage(self, value):
                self.hp -= value
                if self.hp <= 0:
                        self.hp = 0
                        self.isAlive = False
