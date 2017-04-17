

class Cards:
	
	def __init__(self,Display_in,PointValue_in,Suit_in):
		self.DisplayName = Display_in 
		self.PointValue = PointValue_in 
		self.Suit = Suit_in 
	#	self.Image = Image from file
		

	def __str__(self):
		return self.DisplayName

	def rank(self):
		return self.PointValue

	def suit(self):
		return self.Suit	
