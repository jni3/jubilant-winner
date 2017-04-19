import Deck
import bla
import Playerclass
import Cards

class Trick:
    def __init__(self):
        self.trick = []
        self.suit = -1
        self.cardsInTrick = 0
        self.points = 0         #The number of points in this trick
        self.highest = 0
        self.winner = -1

    def __str__(self):
        return str(self.trick)

    def setTrickSuit(self, card): #card is GUI input
        self.suit = card[1]

    def addCard(self,card, i):   #This is playing a card, card has to be entered via GUI, index has to tell which player enters the card
        if(self.cardsInTrick == 0):
            self.setTrickSuit(card)

        self.trick.append(card)	#GUI has to choose a card here
        self.cardsInTrick += 1

	#I assume the card is still a card object here, but in the hand they are converted to tuples..
        if(card[1] == "Hearts"):
            self.points += 1
        elif(card[1] == "Spades" and card[0]==12):
            self.points += 13

        if(card[1] == self.suit):
            if(card[0] > self.highest):
                self.highest = card[0]
                self.winner = i
                

    def winnerRound(self):
        return self.winner

    def pointsRound(self):
        return self.points
