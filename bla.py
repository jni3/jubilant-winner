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

        sortedHand = [clubsRankList, spadesRankList, heartsRankList, diamondsRankList]
        self.hand = sortedHand
        return self.hand	

    def updateHand(self):
        self.hand = sortCardsbyRank()

    def __str__(self):
        return str(self.hand)
		

        

    
