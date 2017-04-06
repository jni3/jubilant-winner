from Cards import Cards
import random

class Deck:
	def __init__(self,NumberOfDecks=1):
		self.cardList = []
		for i in range(NumberOfDecks):
			for x in range(2,15):
				if(x==14):
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

	def deal(self):
		return self.cardList.pop(0)

	def addCards(self,cards):
		self.cardList += cards
	
	def __str__(self):
			
		deckStr = ''
		for card in self.cardList:
			deckStr += card.__str__() + ','
		return deckStr



