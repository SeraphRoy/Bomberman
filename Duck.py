from Global import *
from Img import *
from Enemy import *

class Duck(Enemy):
	def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
		Enemy.__init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary)
		self.charging = False
		self.chargetime = 15
		self.chargeleft = 20
		self.chargeDirection =1
		self.damage = 25
		self.bias = 20

	def Action(self, screen, player, seconds):
		#distance in x direction between player and enemy
			xDistance = player.GetX()-self.rect.x
			#distance in y direction between player and enemy
			yDistance = player.GetY()-self.rect.y

			if self.timetochange>0:
				self.timetochange-=1
			else:
				self.timetochange = 4

			if abs(xDistance)<self.speed/2 and abs(yDistance)<self.speed/2 and player.GetInvincible()<=0:
				player.GetDamge(self.damage)
				player.KnockBack(self.chargeDirection)

			#distance that this move is going to travel
			distance =0;
			self.time+=seconds
			if ((abs(xDistance)<self.radarx and abs(yDistance)<self.bias) or (abs(yDistance)<self.radary and (abs(xDistance)<self.bias))) and self.charging == False:
				self.charging = True
				#chare to x direction
				if abs(xDistance)>abs(yDistance):
					if player.GetX()>self.rect.x:
						self.chargeDirection = 3
					else:
						self.chargeDirection = 1
				#charge to y direction
				else:
					if player.GetY()>self.rect.y:
						self.chargeDirection = 4
					else:
						self.chargeDirection = 2

			#charge time ended
			if self.chargeleft<=0:
				self.charging = False
				self.chargetime = 15
				self.chargeleft = 20
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
					distance = 2*self.rushingSpeed*seconds
					self.chargeleft-=1
					if self.chargeDirection == 1:
						self.image_index = ChangeNextIndex(self.image_index,1)
						if self.rect.x - distance > 0:
							self.rect.x-=distance
						else:
							self.rect.x =0
					elif self.chargeDirection == 3:
						self.image_index = ChangeNextIndex(self.image_index,3)
						if self.rect.x+distance+self.image_x<self.map_x:
							self.rect.x+=distance
						else:
							self.rect.x = self.map_x-self.image_x
					elif self.chargeDirection == 2:
						self.image_index = ChangeNextIndex(self.image_index,2)
						if self.rect.y- distance>0:
							self.rect.y-=distance
						else:
							self.rect.y= 0
					else:
						self.image_index = ChangeNextIndex(self.image_index,4)
						if self.rect.y+distance+self.image_y<self.map_y:
							self.rect.y+=distance
						else:
							self.rect.y = (self.map_y-self.image_y)
			#warning is false, just move up and down
			else:
				distance = seconds * self.speed
				if self.down==True :
					if (self.rect.y+distance)<(self.map_y-self.images[0].get_height()):
						self.rect.y+=distance
						self.lastcommand = 4
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,4)
					else:
						self.down = False
						self.up = True
						self.image_index = 0
				else:
					if (self.rect.y-distance)>0:
						self.rect.y-=distance
						self.lastcommand=2
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,2)
					else:
						self.up = False
						self.down = True
						self.image_index = 4

			
			screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y))
