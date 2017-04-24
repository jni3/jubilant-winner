from PIL import Image

class Cards:

	def __init__(self,PointValue_in,Suit_in):
		self.PointValue = PointValue_in
		self.Suit = Suit_in
		name = str(PointValue_in) + "_of_" + Suit_in.lower()+ ".png"
		self.picture = Image.open("Allcards/"+name)

	def __str__(self):
#                if(self.PointValue_in == 14)
#                        self.PointValue = "Ace"
#                elif(self.PointValue == 13)
#                        self.PointValue = "King"
#                elif(self.PointValue == 12)
#                        self.PointValue = "Queen"
#                elif(self.PointValue == 11)
#                        self.PointValue_in = "Jack"
#				This doesn't work, maybe we can just leave the pointvalues in the code and only use the names in the pictures
                return str(self.PointValue) + " of " + self.Suit

	def rank(self):
		return self.PointValue

	def suit(self):
		return self.Suit

	def getImage(self):
		return self.picture
