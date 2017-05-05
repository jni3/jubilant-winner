from Cards import Cards
import random

class Deck:
	"""Noortje, creates a list of 52 cards which can be shuffled and dealt"""
	def __init__(self):
		self.cardList = []
		
		
	def __str__(self):	
		deckStr = ''
		for card in self.cardList:
			deckStr += card.__str__() + ','
		return deckStr

	def generateDeck(self):
		for x in range(2,15):
			self.cardList.append(Cards(x,"Hearts"))
			self.cardList.append(Cards(x,"Diamonds"))
			self.cardList.append(Cards(x,"Spades"))
			self.cardList.append(Cards(x,"Clubs"))

	def shuffle(self):
		random.shuffle(self.cardList)

	def deal(self):
		return self.cardList.pop(0)
                                                     
	





