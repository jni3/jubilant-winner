import Cards
import Deck

class Hand:
    def __init__(self):
        #preferred over list of ranks, because would have to create more lists
        self.clubs = []
        self.diamonds = []
        self.spades = []
        self.hearts = []

        self.hand = [self.clubs, self.diamonds, self.spades, self.heart]

    def addToListbySuit(self, card): 
        if card.suit == 'Clubs'
            self.clubs.append(card)
        elif card.suit == 'Spades'
            self.spades.append(card)
        elif card.suit == 'Diamond'
            self.diamond.append(card)
        elif card.suit == 'Hearts'
            self.hearts.append(card)
        else:
            print('Please enter a valid card')
            
    def sortCardsbyRank(self, card, suitList):
        clubsRankList = []
        for idx in self.clubs:
            self.clubs[idx].rank.append(clubsRankList)
        clubsRankList.sort(self.clubs)
        self.clubs += clubsRankList 
        
        spadesRankList = []
        for idx in self.clubs:
            self.spades[idx].rank.append(spadesRankList)
        spadesRankList.sort()
        self.spades += spadesRankList
        
        heartsRankList = []
        for idx in self.clubs:
            self.hearts[idx].rank.append(heartsRankList)
        heartsRankList.sort()
        self.hearts += heartsRankList

        diamondsRankList = []
        for idx in self.clubs:
            self.clubs[idx].rank.append(diamondsRankList)
        diamondssRankList.sort()
        self.diamonds+= diamondsRankList

        

    
