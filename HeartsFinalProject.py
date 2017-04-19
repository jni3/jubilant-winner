import Cards
import Deck
from Playerclass import Player
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
        self.currentTrick = Trick.Trick()
        self.trickWinner = -1
        self.heartsBroken = False
        self.losingPlayer = None
        self.passingCards = [[],[],[],[]]
        name = input("Please enter your name: ")
        self.players = [Player(name, False), Player("John"), Player("Mary"), Player("Joey")]


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
            for p in self.players:
                p.hand.addToListbySuit(self.deck.deal())  #actual hand has to be implemented

    def playATrick(self):
        self.currentTrick = Trick.Trick()
        for i in self.players:
            self.currentTrick.addCard(card, index) #GUI has to enter which card is clicked and which player's turn is playing it


    def scoringOfTrick(self):             #updates the score of the player who wins the round
        winner = self.players[self.currentTrick.winnerRound()]
        winner.winnings(self.currentTrick.pointsRound())

    def scoringTotal(self):
        highestScore = 0
        for p in self.players:
            if(p.score > highestScore):
                highestScore = p.score
        return highestScore
