import pygame

class Cards(pygame.sprite.Sprite):

	def __init__(self,PointValue_in,Suit_in):
                super.__init__(self)
		self.PointValue = PointValue_in
		self.Suit = Suit_in
		name = str(PointValue_in) + "_of_" + Suit_in.lower()+ ".png"
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()		
                self.isUp = False
		
	def __str__(self):
		return str(self.PointValue) + " of " + self.Suit

	def rank(self):
		return self.PointValue

	def suit(self):
		return self.Suit

	def getSurfImage(self):
		return self.image

	def getSurfRect(self):
                return self.rect

	def setXCoord(self, xCoord):
                self.rect.x = xCoord
                
        def setYCoord(self, yCoord):
                self.rect.y = yCoord
                
        def getXCoord(self):
                return self.rect.x

        def getYCoord(self):
                return self.rect.y

        def liftUp(self):
                return self.isUp

        def changeUpOrDown(self, TrueOrFalse):
                self.isUp = TrueOrFalse
                
