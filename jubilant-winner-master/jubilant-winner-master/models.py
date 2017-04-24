from Cards import Cards
import random

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
				
				
				self.cardList.append(Cards(Name + " of Hearts", x, "Hearts"))
				self.cardList.append(Cards(Name + " of Diamonds",x,"Diamonds"))
				self.cardList.append(Cards(Name + " of Spades",x,"Spades"))
				self.cardList.append(Cards(Name + " of Clubs",x,"Clubs"))
		
	def shuffle(self):
		random.shuffle(self.cardList)
	
	def __str__(self):
			
		deckStr = ''
		for card in self.cardList:
			deckStr += card.__str__() + ','
		return deckStr

	
def main():
	deck = Deck()
	print(deck)
	deck.shuffle()
	print(deck)
	card = Cards("10 of Hearts", 10, "Hearts")
	print(card)	
main()
