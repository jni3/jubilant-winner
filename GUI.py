import pygame
import Cards
import Deck
import Background 

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)

display_width = 1000
display_height = 1000
clock = pygame.time.Clock()
fps = 30
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hearts')
font pygame.font.

Background = Background('background_image.png', [0, 0])
#press deal button, call dealCards immediately, drawCards four times
#how do you get the playerHand from the player. It belongs to the player class



def 

def drawPlayerCards([playerHand, CardX, CardY, AccumOnX, AccumOnY):
#how would you allow this for multiple cards? how would you actually do it for each card? how would you do this for tuple? 
#suppose when you call a function, a card object is being moved around, how do you associate the card object / tuple being moved around to the cardImage
#when you do passCards function, are you moving card object around or tuple? it becomes a tuple but when? 

    for suitList in playerHand:
        for card in suitList:
            #unless you can somehow access if computer is true or not
                imageName = str(card[0]) + "_of_" + card[1]
                cardImage = CardImage(imageName, cardTuple, CardX, CardY)
                
                cardImage_Surf = pygame.image.load(imageName)
                gameDisplay.blit(cardImage_Surf, (CardX, CardY))
                pygame.display.update()
                CardX += AccumOnX
                CardY += AccumOnY
        return playersCardImages
#how do I associate each cardImage with a tuple            
#initially each hand is a list of card objects
#then when you pass cards, it becomes a list of tuples with associated rank and suit
#need to associate each cardImage with a tuple. Could just associate 
    
def choosePassCards():
    mouse = pygame.mouse_get_pos()
    click = pygame.mouse.get_pressed() #difference between mouse
    cardsChosen = 0
    while (cardsChosen < 3)
        for cardImage in playersCardImages: #does this way take too long.
                    #need a way to access the cardImage when selected beforehand
                    #this method doesn't work
            if (cardImage.xCoord + pixelWidth > mouse[0] > cardImage.xCoord) and (cardImage.ycoord + pixelHeight > mouse[1] > cardImage.ycoord)
                if (click[0] = 1)
                    cardImage.yCoord += 20
                    pygame.display.update()
                    cardImage.setUpOrDown(True)
                    cardsChosen += 1
                if (cardImage.xCoord + pixelWidth > mouse[0] > cardImage.xCoord) and (cardImage.ycoord + pixelHeight > mouse[1] > cardImage.ycoord) and (cardImage.isUpOrDown() = True)
                    if(click[0] == 1]
                    pygame.display.update()
                    cardsChosen -= 1
        #in back-end call passCards function, which for the computers, automatically switches it around. 
    button ("Pass Left") which calls passCards
#need to separate into picking cards to pass, and pressing button after
#need to do it for computer players

def passCards:
    #calls play function


def moveCard(cardImage):

def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    #do you always need to convert surface objects to rectangles

def gameLoop():
listOfCardImages = []                    
    gameStart = False
    passingCards = False
    gameExit = False
    while not gameExit:
        while gameStart == False:
                gameStart = button(deal button) 
                removeButton function()
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        while passingCards == False
           choosePassCards()
            passCards()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                moveCard(CardImage)

def button(msg, x, y, w, h, i, a, action = None)):
mouse = pygame.mouse_get_pos()
click = pygame.mouse.get_pressed()
if display_width /2 + 125 > mouse[0] > display_width/2 and display_height/2 + 50 > mouse[1] > display_width/2:
    pygame.draw.rect(gameDisplay, red, (display_width/2, dislay_height/2, 125, 50))
#don't you have to be within boundaries as well?
if click[0] == 1 and action!= None:
    action()
    return True
else:
    pygame.draw.rect(gameDisplay, bright_red, (display_width/2, display_height/2, 125, 50))
    return False               
newFont = pygame.font.Font("neo-sans.ttf", 40)
textSurf, textRect = text_objects("DEAL!", newFont)
textRect.center = (display_width/2 + (125/2), display_height/2 + (50/2))
gameDisplay.blit(textSurf, textRect)
gameDisplay.fill(white)
gameDisplay.blit(Background.image, BackGround.rect)
                    
if display_width/2 +
    
    pygame.display.update()
    clock.tick(fps)
    pygame.quit()
    quit()

button("DEAL!", x, y, w, h, i, a, drawCards)
button("Pass Left", x, y, w, h, i, a, passLeft)

gameLoop()



