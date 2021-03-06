from Cards import Cards
import random

class Deck:
	def __init__(self):
		self.cardList = []
			for x in range(2,15):
				self.cardList.append(Cards(x,"Hearts")
				self.cardList.append(Cards(x,"Diamonds")
				self.cardList.append(Cards(x,"Spades")
				self.cardList.append(Cards(x,"Clubs")
		
	def shuffle(self):
		random.shuffle(self.cardList)

	def deal(self):
		return self.cardList.pop(0)
                                                     
	def __str__(self):
			
		deckStr = ''
		for card in self.cardList:
			deckStr += card.__str__() + ','
		return deckStr






