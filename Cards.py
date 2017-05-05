from PIL import Image

class Cards:
	"""Noortje, creates Card objects"""
	
	def __init__(self,PointValue_in,Suit_in):
		self.PointValue = PointValue_in
		self.Suit = Suit_in
		name = str(PointValue_in) + "_of_" + Suit_in.lower()+ ".png"
		self.picture = Image.open("Allcards/"+name)

	def __str__(self):
		return str(self.PointValue) + " of " + self.Suit

	def rank(self):
		return self.PointValue

	def suit(self):
		return self.Suit

	def getImage(self):
		return self.picture
