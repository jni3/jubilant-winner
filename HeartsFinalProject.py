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
    """Noortje, Jason, generates a game"""
    def __init__(self):
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
        name = input("Please enter your name: ")
        self.players = [Player(name, False), Player("John"), Player("Mary"), Player("Joey")]

    """Calls a new round and resets values"""
    def newRound(self):
        print("New Round")
        self.deck = Deck.Deck() 
        self.deck.generateDeck()        
        self.deck.shuffle()
        for s in self.players:
            s.resetTrickScore(0)
            s.hand.emptyHand()
        self.dealCards()
        self.roundNum += 1
        self.trickNum = 0
        
        self.heartsBroken = False
        
        self.passingCards = []
        self.passCards()
        self.has2Clubs()

    def dealCards(self):        
        for p in self.players:
            for i in range(13):
                hand = p.playerHand()
                hand.addToListbySuit(self.deck.deal())
                
            hand.sortCardsbyRank()
            p.setHand(hand)
   
    """Handles the passing of 3 cards to an opponent at the beginning of each round"""
    def passCards(self):
        for p in self.players:
            if(p.computerOrNot() == False):
                print(p.playerHand())
                playerPassList = []
                for i in range(3):
                    
                    passCard = (0,0)
                    while(passCard == (0,0)):
                        passCard = p.pick_a_card('pass')
                        cardSuit = p.hand.getCardsinSuitlist(passCard[1])
                        try:
                            cardSuit.remove(passCard)
                            
                    
                        except:
                            print('Please choose a card from your hand')
                            passCard = (0,0)
                    playerPassList.append(passCard) 
                self.passingCards.append(playerPassList)

            elif(p.computerOrNot()):
                hand = p.playerHand()
                listToPass = hand.choosePass(3)
                self.passingCards.append(listToPass)
       
        for i in range(len(self.players)):
            j = (i + self.passes[self.roundNum%4])%4
            for eachCard in self.passingCards[j]:
                 playerHand = self.players[i].playerHand()
                 playerHand.addCardsFromHand(eachCard)
                 self.players[i].setHand(playerHand)

    """Checks which player has the 2 of clubs at the beginning of a round and lets that player start the first trick"""
    def has2Clubs(self):
        for i  in range(len(self.players)):
            hand = self.players[i].playerHand()
            clubsHand = hand.getCardsinSuitlist('Clubs')
            
            if((2, 'Clubs') in clubsHand):
                self.trickWinner = i
        print(self.trickWinner)

    """Calls a new trick and lets all the players play a card. It also checks if the card that is being played is valid"""
    def playATrick(self):
        self.currentTrick = Trick.Trick()
        for i in range(self.trickWinner, self.trickWinner+len(self.players)):
            i = i %4
            if(self.currentTrick.cardsInTrick() == 0):
                x = 'No card played'
            else:
                x = 'Card already played'
        
            print(self.currentTrick.trickSuit())
            print("Cards currently in the trick:\n", self.currentTrick)
            card = self.players[i].play(x, self.currentTrick.trickSuit())
            
            if(self.trickNum == 0):
                while (card[1] == "Hearts" or ((card[0] == 12 and card[1] == 'Spades'))):
                    self.players[i].reAdd(card)
                    card = self.players[i].play(x, self.currentTrick.trickSuit())
            if(not self.heartsBroken and self.currentTrick.cardsInTrick() == 0):
                while(card[1] == "Hearts"):
                    self.players[i].reAdd(card)
                    card = self.players[i].play(x, self.currentTrick.trickSuit())
            if(card[1] == "Hearts"):
                self.heartsBroken = True
            self.currentTrick.addCard(card, i)
            self.currentTrick.scorePoints(card)
            self.currentTrick.trickWinner(card, i)
            
        self.trickNum +=1

    """After each round, checks if somebody collected all 26 points and shot the moon. And subsequently resets the scores of the trick for all players if it happened"""
    def shootMoon(self):
        shot = False
        for s in self.players:
            if(s.playerTrickScore() == 26):
                print("You shot the moon!")           
                shot = True
        if(shot):
            for s in self.players:
                    if(s.trickScore != 26):
                        s.resetTrickScore(26)
                    else:
                        s.resetTrickScore(0)

    """Four functions that keep track of all the scored points. The points scored in a trick, a round and the total score of the players is being monitored"""
    def scoringOfTrick(self):             
        winner = self.players[self.currentTrick.winnerRound()]
        winner.winnings(self.currentTrick.pointsRound())
        self.trickWinner = self.currentTrick.winnerRound()

    def scoringOfRound(self):
        scoringFile = open("Scores.txt", 'a')
        scores = "\n"
        for s in self.players:
            s.winnings(s.playerTrickScore())
            scores += str(s.playerScore()) + "\t"
        scoringFile.write(scores)

    def scoringTotal(self):
        highestScore = -1
        lowestScore = 150
        for p in self.players:
            if(p.playerScore() > highestScore):
                loser = p
                highestScore = p.playerScore()
            if(p.playerScore() < lowestScore):
                winner = p
                lowestScore = p.playerScore()
            self.losingPlayer = loser
            self.winningPlayer = winner
        return highestScore

    def finalScore(self):
        scoringFile = open("Scores.txt", 'r').read()
        print("Final score:")
        print(scoringFile)
        print(self.losingPlayer," lost the game")
        print(self.winningPlayer, " won the game")


    def participants(self):
        return self.players

    """Is the function that actually starts the game"""
    def playGame(self):
        highestScore = 0
        scoringFile = open("Scores.txt", 'w')
        for s in self.players:
            scoringFile.write(str(s) + "\t")

        while (highestScore < maxScore):    
            self.newRound()
            for r in range(totalTricks): 
                self.playATrick() 
                self.scoringOfTrick()
                print(self.currentTrick)
                print(self.currentTrick.winnerRound(), "won the round")
                print('got', self.currentTrick.pointsRound(), 'points')
            self.shootMoon()
            self.scoringOfRound()
            highestScore = self.scoringTotal()
        
        scoringFile.close()
        self.finalScore()
        

#def main():
#    game = Hearts()
#    game.playGame()
#main()


