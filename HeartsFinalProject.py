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
        self.passes = [1,3,2,0]
        self.currentTrick = Trick.Trick()
        self.trickWinner = -1
        self.trickNum = 0
        self.heartsBroken = False
        self.losingPlayer = None
        self.winningPlayer = None
        self.passingCards = []
        self.players = [Player(name, False), Player("John"), Player("Mary"), Player("Joey")]

#do you need a round Num
    def newRound(self):
        deck = Deck.Deck() #every round generates a new deck
	self.deck = deck.generateDeck()        
	self.deck.shuffle()
        self.roundNum += 1
        self.trickNum = 0
        for s in self.players:
            s.resetTrickScore(0)
        self.heartsBroken = False
        self.dealCards()
        self.passingCards = []
        self.passCards()
        self.has2Clubs()

    def passCards(self):
        for p in self.players:
            if(p.computerOrNot() == False):
                for i in range(3):
                    playerPassList = []
                    playerPassList.append(p.pick_a_card()) #how does this work still?
                    self.passingCards.append(playerPassList)

            elif(p.computerOrNot()):
                hand = p.playerHand()
                listToPass = hand.choosePass(3)
                self.passingCards.append(listToPass)

        for i in range(len(self.players)):
            j = (i + self.passes)%4
            for eachCard in self.passingCards[j]:
                 playerHand = self.players[i].playerHand()
                 playerHand.addToListBySuit(eachCard)
                 playerHand.sortCardsbyRank()
                 self.players[i].setHand(playerHand)

    def dealCards(self):        #gets called when you start a new round
        for i in range(13):
            for p in self.players:
                hand = p.playerHand()
                hand.addToListbySuit(self.deck.deal())
                p.setHand(hand)

    def has2Clubs(self):
        for i  in range(len(self.players)):
            hand = self.players[i].playerHand()
            if((2, 'Clubs') in hand[0]):
                self.trickWinner = i

    def playATrick(self):
        self.currentTrick = Trick.Trick()
        for i in range(self.trickWinner, self.trickWinner+len(self.players)):
            i = i %4
            if(self.currentTrick.cardsInTrick() == 0):
                x = 'No card played'
            else:
                x = 'Card already played'
            card = self.players[i].play(x, self.currentTrick.trickSuit())
            if(self.trickNum == 0):
                while (card[1] == "Hearts" or (card[0] == 12 and card[1] == 'Spades'))
                    self.players[i].reAdd(card)
                    card = self.players[i].play(x, self.currentTrick.trickSuit())
            if(not self.heartsBroken and self.currentTrick.cardsInTrick() == 0):
                while(card[1] == "Hearts"):
                    self.players[i].readd(card)
                    card = self.players[i].play(x, self.currentTrick.trickSuit())
            if(card[1] == "Hearts"):
                self.heartsBroken = True
            self.currentTrick.addCard(card, i)
            self.currentTrick.scorePoints(card)
            self.currentTrick.trickWinner(card, i)
        self.trickNum +=1

    def shootMoon(self):
        shot = False
        for s in self.players:
            if(s.trickScore() == 26):
                print("You shot the moon!")
                shot = True
        return shot

    def scoringOfTrick(self):             #updates the score of the player who wins the round
        winner = self.players[self.currentTrick.winnerRound()
        winner.winnings(self.currentTrick.pointsRound())
        self.trickWinner = self.currentTrick.winnerRound()

    def scoringTotal(self):
        highestScore = 0
        lowestScore = 150
        for p in self.players:
            if(p.playerScore > highestScore):
                loser = p
                highestScore = p.playerScore
            if(p.playerScore < lowestScore):
                winner = p
                lowestScore = p.playerScore
            self.losingPlayer = loser
            self.winningPlayer = winner
        return highestScore

    def scoringOfRound(self):
        for s in self.players:
            s.winnings(s.trickScore())


    def finalScore(self):
        print("Final score:")
        for p in self.players:
            print(p)
        print(self.losingPlayer," lost the game")
        print(self.winningPlayer, " won the game")


    def participants(self):
        return self.players
