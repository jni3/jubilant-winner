import Deck
import Cards
import bla
import Playerclass
import Trick
from PIL import Image


def main():
	print("=====Deck test=====")	
	deck = Deck.Deck()
	print(deck)
	print("=====Deck Shuffle=====")
	deck.shuffle()
	print(deck)
	print("=====Deck deal a card=====")
	deal = deck.deal()	
	print(deal)
	

	print("=====Card test=====")
	card = Cards.Cards("10 of Hearts", 10, "Hearts")
	print(card)	
	print(card.rank())
	print(card.suit())
	image = card.getImage()
	image.show()
	card2 = Cards.Cards("5 of Hearts", 5, "Hearts")
	print(card2)
	print(card2.rank())
	print(card2.suit())
	image2 = card2.getImage()
	image2.show()
	
	print("===Card equality test===")
	print "card1 :", card1
	print "card2 :", card2
	print "card1 == card2", card1 == card2
	print "card1 >= card2", card1 >= card2
	print "card1 <= card2", card1 <= card2
	print "card1 < card2", card1 < card2
	print "card1 > card2", card1 > card2
	
	print("===Pass 3 cards===")
	
	
	
	print("=====Deal a hand=====")
	hand = bla.Hand()	
	for i in range(13):
		dealtest = deck.deal()
		print(dealtest)
		hand.addToListbySuit(dealtest)
		deck.addCards([dealtest])
	hand.sortCardsbyRank()
	print(hand)
	

	print("=====Make a player=====")
	player1 = Playerclass.Player("player1")
	player2 = Playerclass.Player("Computer 1")
	player3 = Playerclass.Player("Computer 2")
	player4 = Playerclass.Player('Computer 3")
	print(player1)
	print(player2)			     
	print(player3)
	print(player4)


	print("=====Trick test=====")
	trick = Trick.Trick()
	for i in range(4):
		trick.addCard(hand.chooseRandomCard(), i) 
		print(trick)

	print("Player ", trick.winnerRound(), " won this round")
	print("and he scored ", trick.pointsRound(), " points")
main()


