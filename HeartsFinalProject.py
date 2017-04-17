import Cards
import Deck
import Playerclass
import bla
import Trick


"""Some variables used throughout the program"""
totalTricks = 13
maxScore = 100
cardsToPass = 3

class Hearts:
    def __init__(self):
        self.roundNum = 0
        self.trickNum = 0
        self.dealer = 0
        self.passes = [1,-1,2,0]
        self.currentTrick = Trick()
        self.trickWinner = -1
        self.heartsBroken = False
        self.losingPlayer = None
        self.passingCards = [[],[],[],[]]
        self.players = [P1, P2, P3, P4]
        self.newRound() #Calls a function in the class

    def newRound(self):
        self.deck = Deck.Deck() #every round generates a new deck
        self.deck.shuffle()
        self.roundNum += 1
        self.trickNum = 0
        self.heartsBroken = False
        self.dealCards()
        self.passingCards = [[],[],[],[]]

    def dealCards(self):        #gets called when you start a new round
        for i in range(13):
            for n in self.players:
                Hand n += self.deck.deal()
