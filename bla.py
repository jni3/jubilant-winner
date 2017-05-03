import Cards
import Deck
import random

class Hand:
    def __init__(self):
        self.clubs = []
        self.diamonds = []
        self.spades = []
        self.hearts = []

        self.hand = [self.clubs, self.diamonds, self.spades, self.hearts]

    def __str__(self):
        return str(self.hand)

    def addToListbySuit(self, card):
        if(card.suit() == 'Clubs'):
            self.clubs.append(card)
        elif(card.suit() == 'Spades'):
            self.spades.append(card)
        elif(card.suit() == 'Diamonds'):
            self.diamonds.append(card)
        elif(card.suit() == 'Hearts'):
            self.hearts.append(card)
        else:
            print('Please input a valid card')

    def sortCardsbyRank(self):
        clubsRankList = []
        for idx in self.clubs:
            clubsRankList.append((idx.rank(),idx.suit()))
        clubsRankList.sort()
        self.clubs = clubsRankList
        

        spadesRankList = []
        for idx in self.spades:
            spadesRankList.append((idx.rank(), idx.suit()))
        spadesRankList.sort()
        self.spades = spadesRankList

        heartsRankList = []
        for idx in self.hearts:
            heartsRankList.append((idx.rank(), idx.suit()))
        heartsRankList.sort()
        self.hearts = heartsRankList

        diamondsRankList = []
        for idx in self.diamonds:
            diamondsRankList.append((idx.rank(),idx.suit()))
        diamondsRankList.sort()
        self.diamonds = diamondsRankList

        self.hand = [self.clubs, self.diamonds, self.spades, self.hearts]
    
    def addCardsFromHand(self, card):
        if(card[1] == 'Clubs'):
            self.clubs.append(card)
            self.clubs.sort()
        elif(card[1] == 'Spades'):
            self.spades.append(card)
            self.spades.sort()
        elif(card[1] == 'Diamonds'):
            self.diamonds.append(card)
            self.diamonds.sort()
        elif(card[1] == 'Hearts'):
            self.hearts.append(card)
            self.hearts.sort()
        else:
            print('Please input a valid card')

    #def getCardsinSuitlist(self, suit):
        #want = self. + suit
        #return want

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
