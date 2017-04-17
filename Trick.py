import Deck
import bla
import Playerclass
import Cards

class Trick:
    def __init__(self):
        self.trick = [0,0,0,0]
        self.suit = -1
        self.cardsInTrick = 0
        self.points = 0
        self.highest = 0
        self.winner = -1

    def setTrickSuit(self, card):
        self.suit = card.suit()

    def addCard(self,card,index):
