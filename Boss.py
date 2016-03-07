from Enemy import *
from Global import *
from Bomb import Bomb

flame_image_names = [flame01,flame02,flame03,flame04,flame05,
					 flame06,flame07,flame08,flame09,flame10,
					 flame11,flame12,flame13,flame14,flame15,
					 flame16,flame17,flame18]

rise_flame_names = [rflame01,rflame02,rflame03,rflame04,
					rflame05,rflame06,rflame07,rflame08,
					rflame09,rflame10,rflame11,rflame12,
					rflame13,]

thunder_names = [thunder01,thunder02,thunder03,thunder04,
				 thunder05,thunder06,thunder07,thunder08,
				 thunder09,thunder10,thunder11,thunder12,
				 thunder13,thunder14]


class Boss(Enemy):
	def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
		Enemy.__init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary)
		self.invincible_turn = 0
		self.show = 1;
		#hp and hp image
		self.hp_image = pygame.image.load('img/hp.png').convert_alpha()
		self.hp_image = pygame.transform.scale(self.hp_image, (self.image_x-4,10))
		self.hp = 100

		#throwing bomb in random position
		self.bomb_each_time = 4
		self.bomb_last_time = 4
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

		#rise flame image
		self.rise_flame_images = []
		for name in rise_flame_names:
			temp = pygame.image.load(name).convert_alpha()
			self.rise_flame_images.append(temp)

		#thunder image
		self.thunder_images = []
		for name in thunder_names:
			temp = pygame.image.load(name).convert_alpha()
			self.thunder_images.append(temp)

		#use flame image in time
		self.flame_countdown = 30;
		self.flame_turn = 0

		#rage when damaged, 60% of health
		self.rage = False;

		#rage burst
		self.rage_burst = False;


		#defense flame
		self.defense_countdown = 0;
		self.defense_flame_turn =0;
		self.defense_second_flame_turn =0;

		#thunder
		self.thunder_turn = 0;
		self.thunder_offset_x =0
		self.thunder_offset_y =0

	def GetDamage(self, value):
		if(self.invincible_turn<=0):
			self.invincible_turn = 15;
			self.hp -= value
			if self.hp <= 0:
				self.hp = 0
				self.isAlive = False
			new_width = (self.hp / 100.0) * (self.image_x-4)
			self.hp_image = pygame.transform.scale(self.hp_image, (int(new_width),10))
			if self.hp <25 and self.rage_burst == False:
				self.rage_burst = True
				self.thunder_turn = 14
			if self.hp <60 and self.rage == False:
				self.rage = True
			if self.rage == True and self.defense_flame_turn <=0 and self.defense_second_flame_turn <=0:
				self.defense_flame_turn = 13;


	def LiveAction(self, screen, player, seconds, bomb_map):
		if self.isAlive:
			self.Action(screen, player, seconds, bomb_map)
						
	def Action(self, screen, player, seconds,bomb_map):
		if self.rage_burst == True:
			self.bomb_each_time = 7
			self.speed = 110
		elif self.rage == True:
			self.bomb_each_time = 6
			self.speed = 70
		if self.invincible_turn>0:
			#flashing affect
			if(self.show==1):
				self.show = 0
			else:
				self.show = 1
			self.invincible_turn-=1

		if self.rage == True and self.defense_countdown<=0 and self.defense_flame_turn <=0 and self.defense_second_flame_turn<=0:
			self.defense_countdown = 120;
			self.defense_flame_turn = 13;
		else:
			self.defense_countdown-=1;

		xDistance = player.GetX()-25-self.rect.x
		#distance in y direction between player and enemy
		yDistance = player.GetY()-25-self.rect.y

		distance =0;
		self.time+=seconds

		#use in later throwing phase, place holder
		current_x = 0
		current_y = 0
		dest_x = 0
		dest_y = 0
		change =0

		#countdown and use the flame
		if self.flame_countdown>0:
			self.flame_countdown-=1
		else:
			self.flame_turn = 18;
			self.flame_countdown = 300

		if self.flame_turn>7 and player.GetInvincible()<=0:
			if abs(yDistance)<30 and player.GetInvincible()<=0:
				player.GetDamge(30)
				if xDistance>0:
					player.KnockBack(3)
				else:
					player.KnockBack(1)
			elif abs(xDistance)<30 and player.GetInvincible()<=0:
				player.GetDamge(30)
				if yDistance>0:
					player.KnockBack(4)
				else:
					player.KnockBack(2)

		#first defense damage
		if self.defense_flame_turn>0 :
			if abs(xDistance)<85 and abs(yDistance)<85 and player.GetInvincible()<=0:
				player.GetDamge(30)
				if abs(xDistance) > abs(yDistance):
					if xDistance>0:
						player.KnockBack(3)
					else:
						player.KnockBack(1)
				else:
					if yDistance>0:
						player.KnockBack(4)
					else:
						player.KnockBack(2)

		#second defense flame
		if self.defense_second_flame_turn>0 :
			if abs(xDistance)<120 and abs(yDistance)<120 and player.GetInvincible()<=0:
				player.GetDamge(30)
				if abs(xDistance) > abs(yDistance):
					if xDistance>0:
						print(xDistance)
						player.KnockBack(3)
					else:
						print(xDistance)
						player.KnockBack(1)
				else:
					if yDistance>0:
						player.KnockBack(4)
					else:
						player.KnockBack(2)


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
			self.bomb_last_time = self.bomb_each_time

		if self.throwing>0:
			for i in range(self.bomb_last_time):
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
			for i in range(self.bomb_last_time):
				new_bomb = Bomb(bomb_image,self.bomb_x_array[i]*51,self.bomb_y_array[i]*51,4)
				bomb_map.AddBomb(new_bomb)
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


		if self.invincible_turn<=0 or self.show == 1:
			screen.blit(self.hp_image,(self.rect.x,self.rect.y-13))
			screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y))
		if self.throwing>0:
			for i in range(self.bomb_last_time):
				screen.blit(bomb, (self.current_bomb_x_array[i], self.current_bomb_y_array[i]))
		if self.flame_turn>0:
			self.flame_turn-=1
			current_iamge = self.flameImages[17 - self.flame_turn]
			current_x = 0
			current_y = 0
			while(current_x+50<720):
				screen.blit(current_iamge , (current_x,self.rect.y))
				current_x+=50
			while(current_y+50<720):
				screen.blit(current_iamge , (self.rect.x,current_y))
				current_y+=50

		if self.defense_flame_turn>0:
			if self.defense_flame_turn == 1:
				self.defense_second_flame_turn = 13
			self.defense_flame_turn-=1;
			defense_image = self.rise_flame_images[12-self.defense_flame_turn];
			screen.blit(defense_image, (self.rect.x-30-60,self.rect.y-30))
			screen.blit(defense_image, (self.rect.x-30+60,self.rect.y-30))
			screen.blit(defense_image, (self.rect.x-30,self.rect.y-60-30))
			screen.blit(defense_image, (self.rect.x-30,self.rect.y+60-30))
			screen.blit(defense_image, (self.rect.x-30+60,self.rect.y+60-30))
			screen.blit(defense_image, (self.rect.x-30-60,self.rect.y+60-30))
			screen.blit(defense_image, (self.rect.x-30+60,self.rect.y-60-30))
			screen.blit(defense_image, (self.rect.x-30-60,self.rect.y-60-30))

		if self.defense_second_flame_turn > 0:
			self.defense_second_flame_turn-=1;
			defense_image = self.rise_flame_images[12-self.defense_second_flame_turn];
			screen.blit(defense_image, (self.rect.x-30-80,self.rect.y-30))
			screen.blit(defense_image, (self.rect.x-30+80,self.rect.y-30))
			screen.blit(defense_image, (self.rect.x-30,self.rect.y-80-30))
			screen.blit(defense_image, (self.rect.x-30,self.rect.y+80-30))
			screen.blit(defense_image, (self.rect.x-30+80,self.rect.y+80-30))
			screen.blit(defense_image, (self.rect.x-30-80,self.rect.y+80-30))
			screen.blit(defense_image, (self.rect.x-30+80,self.rect.y-80-30))
			screen.blit(defense_image, (self.rect.x-30-80,self.rect.y-80-30))

		if self.thunder_turn > 0:
			self.thunder_turn-=1;
			thunder_image = self.thunder_images[13-self.thunder_turn]
			thunder_x = self.rect.x +23 + self.thunder_offset_x- thunder_image.get_width()/2
			thunder_y = self.rect.y+ 25 +self.thunder_offset_y-thunder_image.get_height()
			screen.blit(thunder_image,(thunder_x,thunder_y))

			if abs(player.GetX() +25 - (self.rect.x +23 + self.thunder_offset_x)) < 25 and abs(player.GetY()+25 - (self.rect.y+ 25 +self.thunder_offset_y))<25 and player.GetInvincible()<=0:
				player.GetDamge(25);

			if self.thunder_turn ==0:
				self.thunder_offset_x = random.randint(-1,1)*80
				self.thunder_offset_y = random.randint(-1,1)*80
				self.thunder_turn =14




