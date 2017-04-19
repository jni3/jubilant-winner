from bla import Hand

class Player:
    def __init__(self, name, computer = True, score = 0):
        self.name = name
        self.hand = Hand()
        self.score = score
        self.points = []
        self.computer = computer # is it a computer or not
    
    def __str__(self):
        return "Name: " + self.name + " Score: " + str(self.score)
    
    def pick_a_card(self, action):
        card = None
        while card is None:
            card = raw_input (self.name + ", pick a card to" + action + ":")
        return card #allows players to pick a card to play

    def play(self, action = 'play', c=None):
        if(c == None):
            card = self.pick_a_card(action)
        else:
            card = c
        if( not auto):		#Where does this 'auto' come from?
            card = self.hand.pick_a_card(card)
        return card

    def winnings(self, points):
        self.score += points #adds points to player's total after turn
    
    def playerScore(self):
        return self.score
    
    def playerHand(self):
        return self.hand

    def setHand(self, handplayer):
        self.hand = handplayer


