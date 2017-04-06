import Deck
import Cards
import bla
import Playerclass

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

	print("=====Hand test=====")
	hand = bla.Hand()
	hand.addToListbySuit(card)
	hand.addToListbySuit(card2)
	print(hand)

	
	#hand.sortCardsbyRank()

	print("=====Deal a hand=====")
	for i in range(13):
		dealtest = deck.deal()
		print(dealtest)
		hand.addToListbySuit(dealtest)
		print(hand)
		deck.addCards([dealtest])

	
	print("=====Make a player=====")
	player1 = Playerclass.Player("player1")
	print(player1)

main()


