import Deck
import Cards

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
main()
