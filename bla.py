import Cards
import Deck

class Hand:
    def __init__(self):
        #preferred over list of ranks, because would have to create more lists
        self.clubs = []
        self.diamonds = []
        self.spades = []
        self.hearts = []

        self.hand = [self.clubs, self.diamonds, self.spades, self.hearts]

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
            print('Please enter a valid card')
            
    def sortCardsbyRank(self):
        clubsRankList = []
        for idx in self.clubs:
            clubsRankList.append(idx.rank())
        clubsRankList.sort()
        self.clubs += clubsRankList 
        
        spadesRankList = []
        for idx in self.spades:
            spadesRankList.append(idx.rank())
        spadesRankList.sort()
        self.spades += spadesRankList
        
        heartsRankList = []
        for idx in self.hearts:
            heartsRankList.append(idx.rank())
        heartsRankList.sort()
        self.hearts += heartsRankList
        print(self.hearts)
        print(heartsRankList)

        diamondsRankList = []
        for idx in self.diamonds:
            diamondsRankList.append(idx.rank())
        diamondsRankList.sort()
        self.diamonds+= diamondsRankList

    def __str__(self):
        return str(self.hand)
		

        

    
