class Cards:
	"""Makes 1 card at a time, we probably have to use a loop to make them all, or just use the deck"""
	def __init__(self,Display_in,PointValue_in,Suit_in):
		self.DisplayName = Display_in 
		self.PointValue = PointValue_in 
		self.Suit = Suit_in 
		

	def __str__(self):
		return str(self.DisplayName)

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
				
				
				self.cardList.append((Name + " of Hearts", x, "Hearts"))
				self.cardList.append((Name + " of Diamonds",x,"Diamonds"))
				self.cardList.append((Name + " of Spades",x,"Spades"))
				self.cardList.append((Name + " of Clubs",x,"Clubs"))

	def __str__(self):
		return str(self.cardList)	
#class Hand:

#class Player:

	
def main():
	deck = Deck()
	print(deck)
	card = Cards("10 of Hearts", 10, "Hearts")
	print(card)	
main()
