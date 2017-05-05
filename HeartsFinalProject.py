import Cards
import Deck
from Playerclass import Player
import bla
import Trick
import View

"""Some variables used throughout the program"""
totalTricks = 13
maxScore = 100
cardsToPass = 3

class Hearts:
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
   
    def passCards(self):
        for p in self.players:
            if(p.computerOrNot() == False):
                print(p.playerHand())
                playerPassList = []
                    passCard = (0,0)
                    while(passCard == (0,0)):
                        passCard = p.selectCard()
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

    

    def has2Clubs(self):
        for i  in range(len(self.players)):
            hand = self.players[i].playerHand()
            clubsHand = hand.getCardsinSuitlist('Clubs')
            
            if((2, 'Clubs') in clubsHand):
                self.trickWinner = i
        print(self.trickWinner)

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
            View.updatecardLocation(card)
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

    def playGame(self):
        highestScore = 0
        scoringFile = open("Scores.txt", 'w')
        for s in self.players:
            scoringFile.write(str(s) + "\t")
 
        gameExit = False
        gameStart = False
        passingCards = False
        gameDisplay.fill(white) 
        gameDisplay.blit(Background.image, Background.rect)
        while(not gameExit):
            while (highestScore < maxScore): 
                while(gameStart == False):
                        pressedOrNot = View.dealButton("DEAL!", display_width/2, display_height/2, 125, 50, red, bright_red)  
                        pygame.display.update() 
                        gameStart = pressedOrNot

                        for event in pygame.event.get(): 
                            if event.type == pygame.QUIT:
                                gameExit = True
                                gameStart = True
                                passingCards = True
                               
                while(passingCards == False): 
                     passedCards = choosePassCards()
                     pressedOrNot = passButton("Pass Left!", display_width/2, display_height/2, 125, 50, green, bright_green, passedCards)
                     pygame.display.update()
                     passingCards = pressedOrNot

                     for event in pygame.event.get(): 
                            if event.type == pygame.QUIT:
                                gameExit = True
                                passingCards = True

                    for r in range(totalTricks): 
                        self.playATrick() 
                        self.scoringOfTrick()
                        print(self.currentTrick)
                        print(self.currentTrick.winnerRound(), "won the round")
                        print('got', self.currentTrick.pointsRound(), 'points')

                    self.shootMoon()
                    self.scoringOfRound()
                    highestScore = self.scoringTotal()

                    for event in pygame.event.get(): 
                            if event.type == pygame.QUIT:
                                gameExit = True
                                passingCards = True
                
                scoringFile.close()
                self.finalScore()
        

#def main():
#    game = Hearts()
#    game.playGame()
#main()


