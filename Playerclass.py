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
        return self.name

    def pick_a_card(self,action = 'play'):
       
        card = input (self.name + ", pick a card to" + action + ":")
        card = tuple(x for x in card.split(','))
        card = (int(card[0]),card[1])
        
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
                return randomCard
        else:
            card = (0,0)
            print("Choose from your hand:\n", self.hand)
            
            print(trickSuit)
            print(trickSuit[0])
            if(x == 'No card played'):
                card = self.pick_a_card('play')
                cardSuit = self.hand.getCardsinSuitlist(card[1])
                try:
                    cardSuit.remove(card)
                    
                except:
                    print('Please choose a card from your hand')
                    card = (0,0)

            if(x == 'Card already played'):
                if(self.hand.getCardsinSuitlist(trickSuit[0]) != []):
                    while (card[1] != trickSuit[0]):
                        card = self.pick_a_card('play')
                        cardSuit = self.hand.getCardsinSuitlist(card[1])
                        try:
                            cardSuit.remove(card)
                    
                        except:
                            print('Please choose a card from your hand')
                            card = (0,0)
                else:
                    card = self.pick_a_card('play')
                    cardSuit = self.hand.getCardsinSuitlist(card[1])
                    try:
                        cardSuit.remove(card)
                    
                    except:
                        print('Please choose a card from your hand')
                        card = (0,0)
                    
                    
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

