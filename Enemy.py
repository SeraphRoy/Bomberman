import pygame
from pygame.locals import *

class Enemy:
		image_x = 51
		image_y = 51 

		def __init__(self, x,y,speed,rushingSpeed, imagename, radarx, radary):
			temp = pygame.image.load(imagename).convert_alpha()
			self.image = pygame.transform.scale(temp, (self.image_x,self.image_y))
			self.speed = speed
			self.rushingSpeed = rushingSpeed
			self.x = x
			self.y = y
			self.time = 0.5
			self.timeChange = 0.5
			self.radary = radary
			self.radarx = radarx
			self.warning = False
			#0 = left, 1 = right, 2 = up, 3 = down
			self.lastcommand = 0


		def Action(self, screen, player, seconds):
			xDistance = player.GetX()-self.x
			yDistance = player.GetY()-self.y
			self.time+=seconds
			if abs(xDistance)<self.radarx and abs(yDistance)<self.radary:
				warning = True
			else :
				warning = False

			distance = seconds * self.speed

			if(warning):
				if abs(xDistance)>self.speed/2 or abs(yDistance)>self.speed/2:
					if self.time<self.timeChange:
						if self.lastcommand == 0:
							self.x-=distance
						elif self.lastcommand == 1:
							self.x+=distance
						elif self.lastcommand == 2:
							self.y-=distance
						else:
							self.y+=distance
					else:
						self.time = 0;
						if (abs(xDistance)-abs(yDistance))>self.speed/4:
							if xDistance>distance:
								self.x+=distance
								self.lastcommand = 1
							elif xDistance<distance:
								self.x-=distance
								self.lastcommand = 0
						else:
							if yDistance>distance:
								self.y+=distance
								self.lastcommand = 3
							elif yDistance<distance:
								self.y-=distance
								self.lastcommand = 2

			screen.blit(self.image, (self.x, self.y))