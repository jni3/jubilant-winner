from Hand import Hand
import random
import Card
import Trick

class Player:
    def __init__(self, name, computer = True):
        self.name = name
        self.hand = Hand()
        self.score = 0
        self.computer = computer
        self.trickScore = 0

    def __str__(self):
        return "Name: " + self.name + " Score: " + str(self.score)

    def pick_a_card(self, action):
        card = None
        while card is None:
            card = raw_input (self.name + ", pick a card to" + action + ":")
        return card #allows players to pick a card to play
                    #how does this work?

    def reAdd(self, card):
        if(card[1] == 'Hearts' or card[1] == 'Spades')
            self.hand.addToListbySuit(card)
            self.hand.sortCardsbyRank()

    def play(self, action = 'play', c=None, x, trickSuit):
        if(self.computer == True)
            if(x == 'No card played'):
                while True:
                    try:
                        randomSuit = self.hand.chooseRandomSuit()
                        randomCard = self.hand.chooseRandomCard(randomSuit)
                        randomSuit.pop(randomCard)
                        break
                except IndexError:
                    print('Empty list, retrying until valid card')

            return randomCard

            if(x == 'Card already played'):
                randomSuit = ''
                while (randomCard[1] != trickSuit):
                    try:
                    randomSuit = self.hand.chooseRandomSuit()
                    randomCard = self.hand.chooseRandomCard(randomSuit)
                    except IndexError:
                        print('Empty list, retrying until valid card')
                randomSuit.pop(randomCard)
            return randomCard
        else:
            card = self.pick_a_card(action)
            return card
        #still need to figure out how player works.
        #also, how would it work for picking matching suit and heartsbroken rules

    def winnings(self, points):
        self.score += points #adds points to player's total after turn

    def playerScore(self):
        return self.score

    def playerHand(self):
        return self.hand

    def setHand(self, handplayer):
        self.hand = handplayer

    def computerOrNot(self):
        return self.computer

    def setTrickScore(self, points):
        self.trickScore += points

    def resetTrickScore(self, points):
        self.trickScore = points 

    def trickScore(self):
        return self.trickScore
