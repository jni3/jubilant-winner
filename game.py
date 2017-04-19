"""Play the actual game"""

import HeartsFinalProject
import Playerclass

"""Some variables used throughout the program"""
totalTricks = 13
maxScore = 100
cardsToPass = 3

def main():
    game = HeartsFinalProject.Hearts() #initializes the game and deals the first hand
    tricks = 13
    while (game.scoringTotal() < maxScore):    #makes sure you play to a 100 points
        game.newRound()
        for r in range(tricks): # you play 13 tricks
            game.playATrick() # This has to ask all players for a card, these are added to the trick list
            game.scoringOfTrick()
        game.scoringTotal()

main()
