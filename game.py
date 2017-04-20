"""Play the actual game"""

import HeartsFinalProject
import Playerclass

"""Some variables used throughout the program"""
totalTricks = 13
maxScore = 100
cardsToPass = 3

def main():
    name = input("Please enter your name: ")
    game = HeartsFinalProject.Hearts(name) #initializes the game and deals the first hand
    highestScore = 0


    while (highestScore < maxScore):    #makes sure you play to a 100 points
        game.newRound()
        for r in range(totalTricks): # you play 13 tricks
            game.playATrick() # This has to ask all players for a card, these are added to the trick list
            game.scoringOfTrick()
        if(game.shootMoon()):
            players = game.participants()
            for s in players:
                if(s.trickScore != 26):
                    s.setTrickScore(26)
                else:
                    s.setTrickScore(0)
        game.scoringOfRound()
        highestScore = game.scoringTotal()

    game.finalScore()

main()
