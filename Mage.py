from Global import *
from Img import *
from Enemy import *

flame_image_names = [flame01,flame02,flame03,flame04,flame05,
					 flame06,flame07,flame08,flame09,flame10,
					 flame11,flame12,flame13,flame14,flame15,
					 flame16,flame17,flame18]

class Mage(Enemy):
	def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
		Enemy.__init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary)
		self.charging = False
		self.chargetime = 10
		self.damgetime = 18
		self.chargeDirection =1
		self.damage = 50

		#where the mage is placed
		self.magex = 0
		self.magey = 0

		#bias to determine if player is in the same row as Mage
		self.bias = 20

		#image for the flames
		self.flameImages = []
		for name in flame_image_names:
			temp = pygame.image.load(name).convert_alpha()
			self.flameImages.append(temp)
		self.flameIndex = 0


	def Action(self, screen, player, seconds):
		#distance in x direction between player and enemy
			xDistance = player.GetX()-self.x
			#distance in y direction between player and enemy
			yDistance = player.GetY()-self.y

			if self.timetochange>0:
				self.timetochange-=1
			else:
				self.timetochange = 3


			if self.charging == True and self.chargetime ==0 and abs(self.magex-player.GetX())<self.images[5].get_width()/2 and abs(self.magey -player.GetY())<self.images[5].get_height()/2 and player.GetInvincible()<=0:
				player.GetDamge(self.damage)
				player.KnockBack(self.chargeDirection)

			#distance that this move is going to travel
			distance =0;
			self.time+=seconds
			if self.charging == False and ((abs(xDistance)<self.radarx and abs(yDistance)<self.bias) or (abs(yDistance)<self.radary and abs(xDistance)<self.bias)):
				self.charging = True
				#chare to x direction
				if abs(xDistance)>abs(yDistance):
					if player.GetX()>self.x:
						self.chargeDirection = 3
						self.image_index = 12
					else:
						self.chargeDirection = 1
						self.image_index = 8
				#charge to y direction
				else:
					if player.GetY()>self.y:
						self.chargeDirection = 4
						self.image_index = 4
					else:
						self.chargeDirection = 2
						self.image_index = 0

				self.magex = player.GetX()+21
				self.magey = player.GetY()+36

			#charge time ended
			if self.damgetime<=0:
				self.charging = False
				self.chargetime = 10
				self.damgetime = 18
				if self.down == True:
					self.image_index = 4
				else:
					self.image_index = 0

			#if still prepare charging or charging
			if self.charging == True:
				#charging
				if self.chargetime>0:
					self.chargetime-=1

				#start rushing
				else:
					self.damgetime-=1
					current_iamge = self.flameImages[17 - self.damgetime]
					screen.blit(current_iamge , (self.magex-current_iamge.get_width()/2,self.magey-current_iamge.get_height()/2))

			#warning is false, just move up and down
			else:
				distance = seconds * self.speed
				if self.down==True :
					if (self.y+distance)<(self.map_y-self.images[0].get_height()):
						self.y+=distance
						self.lastcommand = 4
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,4)
					else:
						self.down = False
						self.up = True
						self.image_index = 0
				else:
					if (self.y-distance)>0:
						self.y-=distance
						self.lastcommand=2
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,2)
					else:
						self.up = False
						self.down = True
						self.image_index = 4

			
			screen.blit(self.images[self.image_index], (self.x, self.y))