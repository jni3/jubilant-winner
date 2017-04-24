from PIL import Image

class Cards:

	def __init__(self,PointValue_in,Suit_in):
		self.PointValue = PointValue_in
		self.Suit = Suit_in
		name = str(PointValue_in) + "_of_" + Suit_in.lower()+ ".png"
		self.picture = Image.open("Allcards/"+name)

	def __str__(self):
                if(self.PointValue_in == 14)
                        self.PointValue_in = "Ace"
                elif(self.PointValue_in == 13)
                        self.PointValue_in = "King"
                elif(self.PointValue_in == 12)
                        self.PointValue_in == "Queen"
                elif(self.PointValue_in == 11)
                        self.PointValue_in == "Jack"
                return str(PointValue_in) + "of" + Suit_in.lower()

	def rank(self):
		return self.PointValue

	def suit(self):
		return self.Suit

	def getImage(self):
		return self.picture




