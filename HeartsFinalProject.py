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
    def __init__(self, name):
        self.roundNum = 0
        self.trickNum = 0
        self.dealer = 0
        self.passes = [1,-1,2,0]
        self.currentTrick = Trick.Trick()
        self.trickWinner = -1
        self.heartsBroken = False
        self.losingPlayer = None
        self.passingCards = [[],[],[],[]]
        self.players = [Player(name, False), Player("John"), Player("Mary"), Player("Joey")]


    def newRound(self):
        self.deck = Deck.Deck() #every round generates a new deck
        self.deck.shuffle()
        self.roundNum += 1
        self.trickNum = 0
        self.heartsBroken = False
        self.dealCards()
        self.passingCards = [[],[],[],[]]
        self.has2Clubs()

    def dealCards(self):        #gets called when you start a new round
        for i in range(13):
            for p in self.players:
                hand = p.playerHand()
                hand.addToListbySuit(self.deck.deal())  #actual hand has to be implemented
                hand.sortCardsbyRank()
                p.setHand(hand)

    def has2Clubs(self):
        for i  in range(len(self.players)):
            hand = self.players[i].playerHand()
            clubs = hand[0]
            if((2, 'Clubs') in clubs):
                self.trickWinner = i
            
            

    def playATrick(self):
        self.currentTrick = Trick.Trick()
        self.trickNum += 1

        startPlayer = self.players[self.trickWinner]
	startPlayer.play()
        for i in range(self.trickwinner, self.trickWinner+len(self.players)):
            i = i %4
            card = self.players[i].play() #Is a function from the playerclass, how does this work?
            self.currentTrick.addCard(card, i) 


    def scoringOfTrick(self):             #updates the score of the player who wins the round
        winner = self.players[self.currentTrick.winnerRound()]
        winner.winnings(self.currentTrick.pointsRound())
        self.trickWinner = self.currentTrick.winnerRound()

    def scoringTotal(self):
        highestScore = 0
        for p in self.players:
            if(p.score > highestScore):
                loser = p
                highestScore = p.score
            self.losingPlayer = loser
        return highestScore
