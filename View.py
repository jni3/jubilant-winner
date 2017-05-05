import pygame
import HeartsFinalProject

pygame.init()


#colors initialized 
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)

#display properties and display surface initialized
display_width = 1000
display_height = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hearts') 

#initialize clock to be able to define frames per second
clock = pygame.time.Clock() 
clock.tick(30) 

#define font 
buttonFont = pygame.font.Font("neo-sans.ttf", 40) 

#define background image
Background = Background('background_image.jpeg', [0, 0]) 

#define starting hand coordinates for each player
playerstartX = 150
playerstartY = 875
comp2startX = 850
comp2startY = 250
comp2increaseY = 15
comp3startX = 400
comp3startY = 200
comp3increaseX = 15
comp4startX = 200
comp4startY = 300
comp4increaseY = 15
                
def dealButton(msg, x, y, w, h, ic, ac):
    textSurf, textRect = textObjects(msg, buttonFont)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    mouse = pygame.mouse_get_pos()
    click = pygame.mouse.get_pressed()
    if(x+w > mouse[0] > x and y+h > mouse[1] > y):  
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1:
            HeartsFinalProject.newRound()
            drawPlayerCards()
            drawBlankComputerCards(comp2startX, comp2startY, 0, comp2increaseY) 
            drawBlankComputerCards(comp3startX, comp2startY, comp2increaseX, 0) 
            drawBlankComputerCards(comp4startX, comp4startY, 0, comp4increaseY) 
            return True 
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        return False

def passButton(msg, x, y, w, h, ic, c, passedCards)
    textSurf, textRect = textObjects(msg, buttonFont)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    mouse = pygame.mouse_get_pos()
    click = pygame.mouse.get_pressed()
    if(x+w > mouse[0] > x and y+h > mouse[1] > y):  
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1:
            passCards(passedCards)
            drawTransparentCompCards(comp2startX, comp2startY, 0, comp2increaseY) 
            drawTransparentCompCards(comp3startX, comp2startY, comp2increaseX, 0) 
            drawTransparentCompCards(comp4startX, comp4startY, 0, comp4increaseY) 
            pygame.display.update()          
            return gameState = True 
    else:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        return gameState = False

def drawPlayerCards(playersList):
        for suitList in playersList[0].playerHand(): 
            for card in suitList:
                    card.setXCoord(playerstartX)
                    card.setYCoord(playerstartY)
                    gameDisplay.blit(card.getSurfImage(), card.getSurfRect())
                    pygame.display.update()
                    initialX += card.getSurfImage().get_width()
                    card.setXCoord(initialX)

def drawBlankComputerCards(initialX, initialY, changeCardWidth, changeCardHeight):
           blank_card_surf = pygame.image.load('Card_Back.jpg')
           for i in range(13):
               gameDisplay.blit(blank_card_surf, (initialX, initialY))
               pygame.display.update()
           initialX += changeCardWidth
           initialY += changeCardHeight

def drawTransparentCompCards(initialX, initialY, changeCardWidth = 0, changeCardHeight = 0):
    participantsList = self.players[:]
    del participantsList[0]
    for participant in participantsList:
        for suitList in participant.playerHand()
            for card in suitList:
                gameDisplay.blit(card.getSurfImage().convert_alpha(), initialX, initialY)
                pygame.display.update()
                initialX += changeCardWidth
                initialY += changeCardHeight
                
def choosePassCards():
    cardsChosen = 0
    passCardsList = []
    while cardsChosen < 4:
        selectedCard = self.players[0].selectCard()
        selectedCard.changeUpOrDown(True)
        if (selectedCard.liftUp == True):
            liftCard(selectedCard, 30)
            cardsChosen +=1
            passCardsList.append(selectedCard)
        else:
            liftCard(selectedCard, -30)
            selectedCard.changeUpOrDown(False)
            cardsChosen -= 1
            passCardsList.pop(selectedCard)
    return passCardsList

def liftCard(card, changeInY):
    card.getSurfRect.move(x, y)
    gameDisplay.blit(card.getSurfImage(), card.getSurfRect())
    pygame.display.update()
    
def updateCardLocation(card):
    destinationX, destinationY = findCardDestination(card)
    initialXCoord = card.getXCoord()
    initialYCoord = card.getYCoord()
    while (card.getXCoord != destinationX and card.getYCoord != destinationY):
        card.getSurfRect.move(destinationX-initialXCoord/25, destinationY-initialYCoord/25) 
        gameDisplay.blit(card.getSurfImage(), card.getSurfRect) 
        pygame.display.update()

def findCardDestination(card):
        if card == self.players[0].removedCard()
            return destinationX, destinationY = display_width - 100, display_height
        elif card == self.players[1].removedCard()
            return destinationX, destinationY = display_width + 100, display_height
        elif card == self.players[2].removedCard()
            return destinationX, destinationY = display_width, display_height - 100
        else: 
            return destinationX, destinationY = display_width, display_height + 100

def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


    

