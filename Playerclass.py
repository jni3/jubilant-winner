from bla import Hand
import random
import Cards
import Trick
import pygame

class Player:
    def __init__(self, name, computer = True):
        self.name = name
        self.hand = Hand()
        self.score = 0
        self.computer = computer
        self.trickScore = 0
        self.removedCard = None
        
    def __str__(self):
        return self.name

    def selectCard(self):
        gotCard = False
        while gotCard == False:
            pygame.mouse.get_pressed()
            for card in self.hand:
                if card.getSurfRect.collidepoint(pygame.mouse_get_pos()) and click[0] == 1:
                    gotCard = True
        return card
    
    def play(self, x, trickSuit, action = 'play'):
        if(self.computer):
            if(x == 'No card played'):
                while(True):
                    try:
                        randomSuit = self.hand.chooseRandomSuit()
                        randomCard = self.hand.chooseRandomCard(randomSuit)
                        randomCard = randomSuit.pop(randomCard)
                        break
                    except IndexError:     
                        print('Empty list, retrying until valid card')
                self.removedCard = randomCard
                return randomCard

            if(x == 'Card already played'):
                randomTry = [0,0]
                hand = self.hand
                print(hand)
                if(hand.getCardsinSuitlist(trickSuit[0]) != []):
                    while (randomTry[1] != trickSuit[0]): 
                        try:
                            randomSuit = self.hand.chooseRandomSuit()
                            randomCard = self.hand.chooseRandomCard(randomSuit)
                            randomTry = randomSuit[randomCard]
                        except IndexError:
                            print('Something went wrong, retrying until valid card')
                else:
                    while(randomTry == [0,0]):
                        try:
                            randomSuit = self.hand.chooseRandomSuit()
                            randomCard = self.hand.chooseRandomCard(randomSuit)
                            randomTry = randomSuit[randomCard]
                        except IndexError:
                            print('Empty list, retrying until valid card')
                randomCard = randomSuit.pop(randomCard)
                self.removedCard = randomCard
                return randomCard
        else:
            card = (0,0)
            print("Choose from your hand:\n", self.hand)
            
            print(trickSuit)
            print(trickSuit[0])
            if(x == 'No card played'):
                card = self.selectCard()
                cardSuit = self.hand.getCardsinSuitlist(card[1])
                try:
                    cardSuit.remove(card)
                    
                except:
                    print('Please choose a card from your hand')
                    card = (0,0)

            if(x == 'Card already played'):
                if(self.hand.getCardsinSuitlist(trickSuit[0]) != []):
                    while (card[1] != trickSuit[0]):
                        card = self.selectCard()
                        cardSuit = self.hand.getCardsinSuitlist(card[1])
                        try:
                            cardSuit.remove(card)
                    
                        except:
                            print('Please choose a card from your hand')
                            card = (0,0)
                else:
                    card = self.selectCard()
                    cardSuit = self.hand.getCardsinSuitlist(card[1])
                    try:
                        cardSuit.remove(card)
                    
                    except:
                        print('Please choose a card from your hand')
                        card = (0,0)
                    
            self.removedCard = card
            return card
        
    def reAdd(self, card):
        card = (int(card[0]),card[1])
        self.hand.addCardsFromHand(card)

    def winnings(self, points):
        self.score += points 

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

    def removedCard(self):
        return self.removedCard

