import pygame
from pygame.locals import *

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



class Enemy:
		image_x = 51
		image_y = 51 
		map_x = 768
		map_y = 666

		def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):

			if len(imagenames)!=16:
				print("Number of images is wrong")

			self.images = []

			for name in imagenames:
				temp = pygame.image.load(name).convert_alpha()
				temp = pygame.transform.scale(temp, (self.image_x,self.image_y))
				self.images.append(temp)

			self.speed = speed
			self.rushingSpeed = rushingSpeed
			self.rushing = False

			self.x = x
			self.y = y
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

			#for patrol
			self.down = True
			self.up = False


		def Action(self, screen, player, seconds):
			#distance in x direction between player and enemy
			xDistance = player.GetX()-self.x
			#distance in y direction between player and enemy
			yDistance = player.GetY()-self.y

			#distance that this move is going to travel
			distance =0;
			self.time+=seconds
			if abs(xDistance)<self.radarx and abs(yDistance)<self.radary:
				warning = True
			else :
				warning = False

			if abs(xDistance)<self.radarx/2 and abs(yDistance)<self.radary/2:
				self.rushing = True
			else :
				self.rushing = False

			if self.timetochange>0:
				self.timetochange-=1
			else:
				self.timetochange = 4

			if(warning):
				if(self.rushing == True):
					distance = seconds * self.rushingSpeed
				else:
					distance = seconds * self.speed
				if abs(xDistance)>self.speed/2 or abs(yDistance)>self.speed/2:
					if self.time<self.timeChange:
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
						if self.lastcommand == 1 and (self.x- distance)>0:
							self.x-=distance
						elif self.lastcommand == 3 and (self.x + distance)<self.map_x:
							self.x+=distance
						elif self.lastcommand == 2 and (self.y - distance)>0:
							self.y-=distance
						elif (self.y+distance)<self.map_y:
							self.y+=distance
					else:
						self.time = 0;
						if (abs(xDistance)-abs(yDistance))>self.speed/4:
							if xDistance>distance:
								if (self.x + distance)<self.map_x:
									self.x+=distance
								else:
									self.x = self.map_x
								self.lastcommand = 3
							elif xDistance<distance :
								if (self.x- distance)>0:
									self.x-=distance
								else:
									self.x = 0
								self.lastcommand = 1
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)	
						else:
							if yDistance>distance:
								if (self.x- distance)>0:
									self.y+=distance
								else:
									self.y = self.map_y
								self.lastcommand = 4
							elif yDistance<distance:
								if (self.y - distance)>0:
									self.y-=distance
								else:
									self.y = 0
								self.lastcommand = 2
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
			else:
				distance = seconds * self.speed
				if self.down==True :
					if (self.y+distance)<(self.map_y-self.images[0].get_height()):
						self.y+=distance
						self.lastcommand = 4
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
					else:
						self.down = False
						self.up = True
						self.image_index = 0
				else:
					if (self.y-distance)>0:
						self.y-=distance
						self.lastcommand=2
						if self.timetochange==0:
							self.image_index = ChangeNextIndex(self.image_index,self.lastcommand)
					else:
						self.up = False
						self.down = True
						self.image_index = 4
			screen.blit(self.images[self.image_index], (self.x, self.y))