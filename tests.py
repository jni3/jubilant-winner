import Deck
import Cards

def main():
	deck = Deck.Deck()
	print(deck)
	deck.shuffle()
	print(deck)
	card = Cards.Cards("10 of Hearts", 10, "Hearts")
	print(card)	
main()
