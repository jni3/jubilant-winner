import models
import Cards

def main():
	deck = models.Deck()
	print(deck)
	deck.shuffle()
	print(deck)
	card = Cards.Cards("10 of Hearts", 10, "Hearts")
	print(card)	
main()
