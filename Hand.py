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
            
    def add(self,card):
        self.Cards.append(card)

    def sortCardsbyRank(self):
        clubsRankList = []
        for idx in self.clubs:
            clubsRankList.append((idx.rank(),idx.suit()))
        clubsRankList.sort()

        spadesRankList = []
        for idx in self.spades:
            spadesRankList.append((idx.rank(), idx.suit()))
        spadesRankList.sort()

        heartsRankList = []
        for idx in self.hearts:
            heartsRankList.append((idx.rank(), idx.suit()))
        heartsRankList.sort()

        diamondsRankList = []
        for idx in self.diamonds:
            diamondsRankList.append((idx.rank(),idx.suit()))
        diamondsRankList.sort()

        self.hand = [clubsRankList, diamondsRankList, spadesRankList, heartsRankList]

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
            randomSuit = self.chooseRandomSuit()
            removedCard = self.chooseRandomCard(randomSuit)
            remove = randomSuit.pop(removedCard)         #This only deletes the card from the local hand, not the global one
            tempList.append(remove)
        return tempList
