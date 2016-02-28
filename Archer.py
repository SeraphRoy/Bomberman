from Enemy import *
from Img import *


arrow_image_names = [arrow1,arrow2,arrow3,arrow4
			  ,arrow5,arrow6,arrow7,arrow8
			  ,arrow9,arrow10,arrow11,arrow12]

def ChangeNextIndexArcher(current, key):
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
				return 1
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
				return 5
			else:
				return current+1
		else:
			return 5

class Archer(Enemy):
	#same init as Enemy
	def __init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary):
		Enemy.__init__(self, x,y,speed,rushingSpeed, imagenames, radarx, radary)
		self.arrowImages = []
		for name in arrow_image_names:
			temp = pygame.image.load(name).convert_alpha()
			self.arrowImages.append(temp)

		self.damage = 25

		self.lock = False

		self.arrowDirection = 0
		self.arrowSpeed = 450
		self.arrowX = 0
		self.arrowY = 0
		self.arrowTurn = 0
		self.backTurn = 0
		self.waitturn = 0

		#bias to determine if player is in the same row as Mage
		self.bias = 20

	def LiveAction(self, screen, player, seconds):
		if self.isAlive:
			self.Action(screen, player, seconds)
				
	def Action(self, screen, player, seconds):
		#distance in x direction between player and enemy
		xDistance = player.GetX()-self.rect.x
		#distance in y direction between player and enemy
		yDistance = player.GetY()-self.rect.y

		#time to change the image of the archer
		if self.timetochange>0:
			self.timetochange-=1
		else:
			self.timetochange = 4

		#damage calcution
		if self.arrowTurn>0 and abs(self.arrowX-player.GetX())<self.arrowImages[1].get_width()/2 and abs(self.arrowY -player.GetY())<self.arrowImages[1].get_height()/2 and player.GetInvincible()<=0:
			player.GetDamge(self.damage)
			player.KnockBack(self.arrowDirection)

		#0 = left, 1 = right, 2 = up, 3 = down, order of the archer's iamge
		#check if archer can lock the player
		if self.lock == False and self.arrowTurn<=0:
			if (abs(xDistance)<self.radarx and abs(yDistance)<self.bias):
				self.lock = True
				if xDistance>0:
					self.arrowDirection = 3
					self.image_index = 12
				else:
					self.arrowDirection = 1
					self.image_index = 8
			if abs(yDistance)<self.radary and abs(xDistance)<self.bias:
				self.lock = True
				if yDistance>0:
					self.arrowDirection = 4
					self.image_index = 4
				else:
					self.arrowDirection = 2
					self.image_index = 0

			if self.lock == True:
				self.arrowX = self.rect.x
				self.arrowY = self.rect.y
				self.waitturn = 5

		#when lock the player, wait for 2 turns then shot the arrow
		if self.lock == True:
			if self.waitturn>0:
				self.waitturn-=1
			else:
				self.lock = False
				self.backTurn = 7
				self.arrowTurn = 12
		#warning is false
		elif self.backTurn<=0:
			distance = seconds * self.speed
			#move down
			if self.down==True :
				if (self.rect.y+distance)<(self.map_y-self.images[0].get_height()):
					self.rect.y+=distance
					self.lastcommand = 4
					if self.timetochange==0:
						self.image_index = ChangeNextIndexArcher(self.image_index,self.lastcommand)
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
						self.image_index = ChangeNextIndexArcher(self.image_index,self.lastcommand)
				else:
					self.up = False
					self.down = True
					self.image_index = 4

		backupDistance = 70 * seconds
		if self.backTurn > 0:
			self.backTurn-=1
			if self.arrowDirection == 1:
				if (self.rect.x + backupDistance) <650:
					self.rect.x+=backupDistance
				else:
					self.rect.x = 650
			elif self.arrowDirection == 3:
				if (self.rect.x - backupDistance) > 0:
					self.rect.x -= backupDistance
				else:
					self.rect.x = 0
			elif self.arrowDirection == 2:
				if (self.rect.y +backupDistance) < 650:
					self.rect.y += backupDistance
				else:
					self.rect.y = 650
			else :
				if (self.rect.y - backupDistance) > 0:
					self.rect.y -= backupDistance
				else:
					self.rect.y = 0

		#need to update the arrow's position and display the arrow's iamge
		if self.arrowTurn>0:
			arrowDistance = self.arrowSpeed * seconds;
			self.arrowTurn-=1;
			currentArrowImage = self.arrowImages[11-self.arrowTurn]

			if self.arrowDirection == 3:
				if (self.arrowX + arrowDistance) <650:
					self.arrowX+=arrowDistance
				else:
					self.arrowX = 650
					#arrow disappear when hit the bounderary
					self.arrowTurn = 0
			elif self.arrowDirection == 1:
				currentArrowImage = pygame.transform.rotate(currentArrowImage, -180)
				if (self.arrowX - arrowDistance) > 0:
					self.arrowX -= arrowDistance
				else:
					self.arrowX = 0
					self.arrowTurn =0
			elif self.arrowDirection == 4:
				currentArrowImage = pygame.transform.rotate(currentArrowImage, -90)
				if (self.arrowY +arrowDistance) < 650:
					self.arrowY += arrowDistance
				else:
					self.arrowY = 650
					self.arrowTurn =0
			else :
				currentArrowImage = pygame.transform.rotate(currentArrowImage, 90)
				if (self.arrowY - arrowDistance) > 0:
					self.arrowY -= arrowDistance
				else:
					self.arrowY = 0
					self.arrowTurn =0
			screen.blit(currentArrowImage,(self.arrowX,self.arrowY));

		#displaye image on screen
		screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y))




