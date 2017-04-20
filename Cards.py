from PIL import Image

class Cards:

	def __init__(self,Display_in,PointValue_in,Suit_in):
		self.DisplayName = Display_in
		self.PointValue = PointValue_in
		self.Suit = Suit_in
		name = str(PointValue_in) + "_of_" + Suit_in.lower()+ ".png"
		self.picture = Image.open("Allcards/"+name) #in the Allcards folder


	def __str__(self):
		return self.DisplayName

	def rank(self):
		return self.PointValue

	def suit(self):
		return self.Suit

	def getImage(self):
		return self.picture
