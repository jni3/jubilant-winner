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

    def setTrickSuit(self, card): #card is GUI input
        self.suit = card.suit()

    def addCard(self,card, index):   #This is playing a card, card has to be entered via GUI, index has to tell which player enters the card
        if(self.cardsInTrick == 0):
            self.setTrickSuit(card)

        self.trick.append(card)
        self.cardsInTrick += 1

        if(card.suit() == "Hearts"):
            self.points += 1
        elif(card.suit() == "Spades" and card.rank()==12):
            self.points += 13

        if(card.suit() == self.suit):
            if(card.rank() > self.highest):
                self.highest = card.rank()
                self.winner = index

    def winner(self):
        return self.winner

    def points(self):
        return self.points
