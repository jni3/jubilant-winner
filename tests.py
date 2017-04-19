import Deck
import Cards
import bla
import Playerclass
import Trick


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
	deck.addCards([deal])
	print(deck)
	
	

	print("=====Card test=====")
	card = Cards.Cards("10 of Hearts", 10, "Hearts")
	print(card)	
	print(card.rank())
	print(card.suit())
	
	card2 = Cards.Cards("5 of Hearts", 5, "Hearts")

	
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
	print(player1)


	print("=====Trick test=====")
	trick = Trick.Trick()
	for i in range(4):
		trick.addCard(hand.chooseRandomCard(), i) 
		print(trick)

	print("Player ", trick.winnerRound(), " won this round")
	print("and he scored ", trick.pointsRound(), " points")
main()


