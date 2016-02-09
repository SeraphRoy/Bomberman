from Enemy import *

class Ghost(Enemy):
	def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
		Enemy.__init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary)

	def Action(self, screen, player, seconds):
			#distance in x direction between player and enemy
			xDistance = player.GetX()-self.rect.x
			#distance in y direction between player and enemy
			yDistance = player.GetY()-self.rect.y

			#distance that this move is going to travel
			distance =0;
			self.time+=seconds

			#player is inside Ghost's radar
			if abs(xDistance)<self.radarx and abs(yDistance)<self.radary:
				warning = True
			else :
				warning = False

			#player is in inner radar, rushing mode
			if abs(xDistance)<self.radarx/2 and abs(yDistance)<self.radary/2:
				self.rushing = True
			else :
				self.rushing = False

			#when time to change =0, ghost will change the direction
			if self.timetochange>0:
				self.timetochange-=1
			else:
				self.timetochange = 4

			if(warning):
				#calculate the distance based on the current mode
				if(self.rushing == True):
					distance = seconds * self.rushingSpeed
				else:
					distance = seconds * self.speed
				#when ghost does not hit player
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
			#warning is false
			else:
				distance = seconds * self.speed
				#move down
				if self.down==True :
					if (self.rect.y+distance)<(self.map_y-self.images[0].get_height()):
						self.rect.y+=distance
						self.lastcommand = 4
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
					else:
						self.down = False
						self.up = True
						self.image_index = 0
						#move up
				else:
					if (self.rect.y-distance)>0:
						self.rect.y-=distance
						self.lastcommand=2
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
					else:
						self.up = False
						self.down = True
						self.image_index = 4
			screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y))
