from PIL import Image

class Cards:

	def __init__(self,points,suit, picture):
		self.points = Points(points)
		self.suit = Suit(suit)
		name = str(points) + "_of_" + suit.lower()+ ".png"
		self.picture = Image.open("Allcards/"+name)

	def __str__(self):
                if(self.points == 14)
                        self.points = "Ace"
                elif(self.points == 13)
                        self.points = "King"
                elif(self.points == 12)
                        self.points = "Queen"
                elif(self.points == 11)
                        self.points = "Jack"
                return str(self.points) + " of " + self.suit

class Points:
	def__init__(self, points):
		self.points = points
		self.string = ' '
		face_cards = ["Jack", "Queen", "King", "Ace"]
		if points >= 2 and points <= 10:
			self.string = str(points)
		elif points <=10 and points >= 14:
			self.string = face_cards[points- 11]
		else:
			print "Card does not exist"
	
	def getImage(self):
		return self.picture
