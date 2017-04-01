class Cards:
	def __init__(self,Display_in,PointValue_in,Suit_in):
		self.DisplayName = Display_in #"king of Hearts, 10 of Hearts"
		self.PointValue = PointValue_in # 1-13
		self.Suit = Suit_in #Hearts, Clubs, Spades, Diamonds

class Deck:
	def __init__(self,NumberOfDecks=1):
		self.cardList = []
		for i in range(NumberOfDecks):
			for x in range(1,14):
				if(x==1):
					Name="Ace"
				elif(x==11):
					Name="Jack"
				elif(x==12):
					Name="Queen"
				elif(x==13):
					Name="King"
				else:
					Name=str(x)
				self.cardList.append((Name + " of Hearts",x,"Hearts"))
				self.cardList.append((Name + " of Diamonds",x,"Diamonds"))
				self.cardList.append((Name + " of Spades",x,"Spades"))
				self.cardList.append((Name + " of Clubs",x,"Clubs"))

	def __str__(self):
		return str(self.cardList)	
	
def main():
	deck = Deck()
	print(deck)
main()
