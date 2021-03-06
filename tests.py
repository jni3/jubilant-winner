import Deck
import Cards
import bla
import Playerclass
import Trick
from PIL import Image
from HeartsFinalProject import Hearts

def main():
	print("=====Deck test=====")	
	deck = Deck.Deck()
	deck.generateDeck()
	print(deck)
	print("=====Deck Shuffle=====")
	deck.shuffle()
	print(deck)
	print("=====Deck deal a card=====")
	deal = deck.deal()	
	print(deal)
	

	print("=====Card test=====")
	card1 = Cards.Cards(10, "Hearts")
	print(card1)	
	print(card1.rank())
	print(card1.suit())
	image1 = card1.getImage()
	image1.show()
	card2 = Cards.Cards(5, "Hearts")
	print(card2)
	print(card2.rank())
	print(card2.suit())
	image2 = card2.getImage()
	image2.show()
	
	print("=====Hand test=====")
	hand = bla.Hand()
		
	for i in range(13):
		dealtest = deck.deal()
		print(dealtest)
		hand.addToListbySuit(dealtest)
		
		
	hand.sortCardsbyRank()
	
	print(hand)
	smallHand = hand.getCardsinSuitlist('Clubs')
	print(smallHand)

	print("======Pass cards=====")
	print(hand.choosePass(3))
	

	print("=====Make a player=====")
	w = str(input("What is your name?: "))
	player1 = Playerclass.Player(w, False)
	player2 = Playerclass.Player("Computer 1")
	print(player1)
	print(player2)

	print("=====Player attributes=====")
	#Play a card has to be done with GUI
	print("Players score: ", player1.playerScore())
	print("Players trick score: ", player1.playerTrickScore())
	player1.resetTrickScore(5)
	print("Players trick score: ", player1.playerTrickScore())
	player1.setTrickScore(7)
	print("Players trick score: ", player1.playerTrickScore())
	player1.winnings(player1.playerTrickScore())
	print("Players score: ", player1.playerScore())
	print("Players hand: ", player2.playerHand())
	player2.setHand(hand)
	print("Players hand: ", player2.playerHand())
	player2.reAdd((5,'Hearts'))
	print("Players hand: ", player2.playerHand())	
	print("Player is a computer: ", player1.computerOrNot())

	print("=====Computer plays a card=====")
	#User playing a card requires the GUI
	print('--When no card is played--')
	x = 'No card played'
	playedCard = player2.play(x, ('Hearts', 4))
	print(playedCard)
	print('--When a card has been played--')
	x = 'Card already played'
	playedCard = player2.play(x, ('Hearts',4))
	print(playedCard)
	
	print("=====Trick test=====")
	trick = Trick.Trick()
	for i in range(4):
		card = hand.choosePass(1)
		card = card[0]				
		trick.addCard(card, i) 
		trick.scorePoints(card)
		trick.trickWinner(card,i)
		print(trick)

	print("--Info about the trick--")
	print("Number of cards in the Trick: ", trick.cardsInTrick())
	print("Trick suit: ", trick.trickSuit())


	print("Player ", trick.winnerRound(), " won this round")
	print("and he scored ", trick.pointsRound(), " points")

	print("=====Game test=====")
	game = Hearts()
	game.newRound()
	players = game.participants()
	for p in players:
		print(p.name)
		print(p.hand)
	game.playATrick()
	print("Cards in the trick:", game.currentTrick)
	print("Points in the trick:", game.currentTrick.pointsRound())
	print("Winner of the trick:", game.currentTrick.winnerRound())
	for p in players:
		print(p.name)
		print(p.hand)


	print("---Shooting the moon---")	
	players[0].resetTrickScore(26)
	for p in players:	
		print(p.playerTrickScore())
	game.shootMoon()
	for p in players:
		print(p.playerTrickScore())

	print("---Scoring---")
	game.scoringOfTrick()
	game.scoringOfRound()
	game.scoringTotal()
	game.finalScore()

	print("\n\n\n=====The actual game=====")
	game.playGame()
	
main()



