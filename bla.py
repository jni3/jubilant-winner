import Cards
import Deck
import random

class Hand:
    def __init__(self):
        self.Clubs = []
        self.Diamonds = []
        self.Spades = []
        self.Hearts = []

        self.hand = [self.Clubs, self.Diamonds, self.Spades, self.Hearts]

    def __str__(self):
        return str(self.hand)

    def addToListbySuit(self, card):
        if(card.suit() == 'Clubs'):
            self.Clubs.append(card)
        elif(card.suit() == 'Spades'):
            self.Spades.append(card)
        elif(card.suit() == 'Diamonds'):
            self.Diamonds.append(card)
        elif(card.suit() == 'Hearts'):
            self.Hearts.append(card)
        else:
            print('Please input a valid card')

    def sortCardsbyRank(self):
        clubsRankList = []
        for idx in self.Clubs:
            clubsRankList.append((idx.rank(),idx.suit()))
        clubsRankList.sort()
        self.Clubs = clubsRankList
        

        spadesRankList = []
        for idx in self.Spades:
            spadesRankList.append((idx.rank(), idx.suit()))
        spadesRankList.sort()
        self.Spades = spadesRankList

        heartsRankList = []
        for idx in self.Hearts:
            heartsRankList.append((idx.rank(), idx.suit()))
        heartsRankList.sort()
        self.Hearts = heartsRankList

        diamondsRankList = []
        for idx in self.Diamonds:
            diamondsRankList.append((idx.rank(),idx.suit()))
        diamondsRankList.sort()
        self.Diamonds = diamondsRankList

        self.hand = [self.Clubs, self.Diamonds, self.Spades, self.Hearts]
    
    def addCardsFromHand(self, card):
        if(card[1] == 'Clubs'):
            self.Clubs.append(card)
            self.Clubs.sort()
        elif(card[1] == 'Spades'):
            self.Spades.append(card)
            self.Spades.sort()
        elif(card[1] == 'Diamonds'):
            self.Diamonds.append(card)
            self.Diamonds.sort()
        elif(card[1] == 'Hearts'):
            self.Hearts.append(card)
            self.Hearts.sort()
        else:
            print('Please input a valid card')
        
        self.hand = [self.Clubs, self.Diamonds, self.Spades, self.Hearts]

    def getCardsinSuitlist(self, suit):
        return getattr(self, suit)

    def chooseRandomSuit(self):
        randomSuit = random.choice(self.hand)
        return randomSuit

    def chooseRandomCard(self, randomSuit):
        randomCard = random.choice(randomSuit)
        randomCardIndex = randomSuit.index(randomCard)
        return randomCardIndex

    def choosePass(self, numOfPass):
        tempList = []
        for i in range(numOfPass):
            t = True
            while(t == True):
                try:
                    randomSuit = self.chooseRandomSuit()
                    removedCard = self.chooseRandomCard(randomSuit)
                    remove = randomSuit.pop(removedCard)        
                    tempList.append(remove)
                    t = False
                except:
                    print("oops something went wrong")
                
        return tempList
