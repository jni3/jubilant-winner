from bla import Hand
import random
import Cards
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

    def pick_a_card(self, trickSuit, action):
        while(True):
            card = raw_input (self.name + ", pick a card to" + action + ":")
            if(self.hand[trickSuit[1]] != []):
                if(card[1] == trickSuit[0]):
                    return card
                else:
                    print("You have to play the asked suit, try again!")
            else:
                return card
        #allows players to pick a card to play
                    #how does this work?

    def reAdd(self, card):
        self.hand.addToListbySuit(card)
        self.hand.sortCardsbyRank()

    def play(self, x, trickSuit,action = 'play', c=None):
        if(self.computer):
            if(x == 'No card played'):
                while(True):
                    try:
                        randomSuit = self.hand.chooseRandomSuit()
                        randomCard = self.hand.chooseRandomCard(randomSuit)
                        randomCard = randomSuit.pop(randomCard)
                        break
                    except IndexError:      #Does this have to have same indentation
                        print('Empty list, retrying until valid card')

                return randomCard

            if(x == 'Card already played'):
                randomTry = []
                hand = list(self.hand)
                print(hand)
                index = trickSuit[1]
                if(hand[index] != []):
                    while (randomTry[1] != trickSuit[0]): #Might break if index 1 is non existent
                        try:
                            randomTry = self.hand.choosePass(1)
                            #randomSuit = self.hand.chooseRandomSuit()
                            #randomCard = self.hand.chooseRandomCard(randomSuit)
                            #randomTry = randomSuit[randomCard]
                        except IndexError:
                            print('Empty list, retrying until valid card')
                else:
                    while(randomTry == []):
                        try:
                            randomTry = self.hand.choosePass(1)
                            #randomSuit = self.hand.chooseRandomSuit()
                            #randomCard = self.hand.chooseRandomCard(randomSuit)
                            #randomTry = randomSuit[randomCard]
                        except IndexError:
                            print('Empty list, retrying until valid card')
                #randomCard = randomSuit.pop(randomCard)
                return randomTry[0]
        else:
            card = self.pick_a_card(trickSuit, 'play')
            return card
        #still need to figure out how player works.
        #also, how would it work for picking matching suit and heartsbroken rules
        #picking matching suit should be implemented in the pick a card function I think, the same way you did it for the computer
        #Hearts broken should also just be a condition where you check if self.heartsbroken is True or False in both the computer player choosing and the player choosing

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

    def playerTrickScore(self):
        return self.trickScore

