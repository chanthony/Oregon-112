#QUIZX
import random

def generateQuizX(data):
    quizXTypes = [["OOP","Dictionaries","112","sets","lists","recursion",
                    "Kosbie","Stehlik"],["tetris","loops","strings","tkinter",
                    "python","style","code tracing","functions"]]
    #each quizX is stored as a list element consisting of a bunch of strings
    quizXType = random.choice(quizXTypes)#pick one of the two types
    data.currentQuizX = QuizX(data,quizXType)#create and store that quizx

class QuizX(object):
    def __init__(self,data,cardList):
        self.cardTypes = cardList#the list of card contents
        self.cardBack = data.cardBack#the back of the card image
        self.clickedCard = None#the card we currently have selected
        self.secondCard = None
        self.twoCardsUp = False#if we have two cards picked
        self.passed = False#the player hasn't passed yet
        self.guesses = 0
        self.generateCards(data)

    def generateCards(self,data):
        self.cardList = [None] * 16#start out as an empty list
        for cardType in self.cardTypes:#for each of the 8 pairs
            card1Index = self.pickIndex()#pick a card location
            card1 = self.createCard(cardType,card1Index,data)#create card
            self.cardList[card1Index] = card1#store the card in that location
            card2Index = self.pickIndex()#repeat for the second card
            card2 = self.createCard(cardType,card2Index,data)
            self.cardList[card2Index] = card2
            card1.partner = card2#attach the two cards to each other
            card2.partner = card1

    def pickIndex(self):#recursively picks an index
        possibleIndices = []
        for index in range(0,16):
            if self.cardList[index] == None:#if this spot is empty
                possibleIndices.append(index)#keep track of it
        if possibleIndices == []:
            assert True == False
        return random.choice(possibleIndices)#pick a random index and return it

    def createCard(self,cardType,index,data):
        row = index // 8#each row is 8 cards
        col = index % 8#the location on each row
        if row%2 == 0:#if it's the first row
            y = 80 + self.cardBack.height()/2#the y location of the card
        else:#if it's in the second row
            y = 300 + self.cardBack.height()/2
        #The x is the white space + the other whole cards plus half of this card
        x = (4 * (col + 1)) + self.cardBack.width()*col+self.cardBack.width()/2
        return Card(cardType,x,y,data)#create and return that card

    def quizXMousePressed(self,event,data):
        currentCard = None#start out with no card selected
        for card in self.cardList:#check to see if we hit a card
            if card != None and card.cardClicked(event):#if we clicked this card
                currentCard = card#keep track of that card
        if currentCard == None:#if we didn't click anything
            pass#no pointin checking the rest of this stuff
        elif self.clickedCard == None:#if nothing is already clicked
            self.clickedCard = currentCard#keep track of this new card
            currentCard.up = True#turn this card face up
        elif self.twoCardsUp == False:#theres something clicked already
            self.guesses += 1#increment our guesses by one
            currentCard.up = True#turn this card up
            self.twoCardsUp = True#we now have two cards clicked
            self.secondCard = currentCard#keep track of this new card
            if currentCard.isPair(self.clickedCard):
                self.removePair(currentCard,self.clickedCard)#remove the pair
        else:#we already clicked two cards
            self.clickedCard.up = self.secondCard.up = False#flip the cards over
            self.clickedCard = self.secondCard = None#forget the previous cards
            self.twoCardsUp = False#we no longer have two cards picked
            self.quizXMousePressed(event,data)#call the function again

    def removePair(self,card1,card2):
        #finds the pair and then removes them while preserving indices
        card1Index = self.cardList.index(card1)#find the cards
        card2Index = self.cardList.index(card2)
        self.cardList[card1Index] = None#replace them with none
        self.cardList[card2Index] = None

    def redrawQuizX(self,canvas,data):
        for index in range(len(self.cardList)):#for each spot
            if self.cardList[index] != None:#if this spot is not empty
                self.cardList[index].drawCard(canvas)#draw that card
        canvas.create_text(data.width/2,40,text="Quiz X time!",fill="white"
                            , font = "Arial 16")
        canvas.create_text(data.width/2,60,text="""Match all the cards in 16 \
guesses or less to pass!""",
                            fill = "white",font="Arial 12")
        guessCount = "Guesses: %d" % self.guesses#display current # of guesses
        canvas.create_text(data.width - 50,50,text = guessCount,fill="white")
        if self.passed == True:#if we won
            canvas.create_text(data.width/2,data.height/2,text="""QuizX Done!
Press Enter to move on!""",fill = "white",font="Arial 28")

    def finishedQuizX(self):#checks win conditions
        for card in self.cardList:
            if card != None:#if any card is still on the board
                return False
        return True#every card must have been found

    def quizXTimerFired(self,data):#really only checks the win conditions
        if self.finishedQuizX():#if the player won
            self.passed = True

    def quizXKeyPressed(self,event,data):
        #if we press enter and we already passed
        if event.keysym == "Return" and self.passed == True:
            self.quizXEndSequence(data)

    def quizXEndSequence(self,data):#the transition into the next mode
        data.mode = "Town"#move to the town
        self.quizXGrader(data)#grade the quizzes and adjust grades
        data.currentQuizX = None#delete this quiz

    def quizXGrader(self,data):
        #grades change based on guesses over/under par but only up to 20 points
        gradeImpact = max(min(((self.guesses - 16) * 5),20),-20)
        for character in data.characterList:
            if gradeImpact > 0:
                character.increaseGrade(gradeImpact)
            elif gradeImpact < 0:
                character.reduceGrade(gradeImpact)


class Card(object):
    def __init__(self,name,x,y,data,partner=None):
        self.name = name#what the contents of the card are
        self.x = x#the center of the card
        self.y = y
        self.partner = partner#the matching card
        self.cardBack = data.cardBack#store the image
        self.up = False#is this card turned over or not

    def getBounds(self):
        x0 = self.x - self.cardBack.width()/2#the left bound of the card
        x1 = self.x + self.cardBack.width()/2#right bound of the card
        y0 = self.y - self.cardBack.height()/2#top of the card
        y1 = self.y + self.cardBack.height()/2#bottom of the card
        return(x0,y0,x1,y1)

    def cardClicked(self,event):#was this card clicked?
        (x0,y0,x1,y1) =self.getBounds()#find the borders of this card
        if event.x >= x0 and event.x <= x1:#if it's horizontally within card
            if event.y >= y0 and event.y <= y1:#vertical intersection
                return True
        return False#we did not click this card

    def drawCard(self,canvas):
        if self.up == False:#if the card is face down
            canvas.create_image(self.x,self.y,image= self.cardBack)#draw back
        else:
            (x0,y0,x1,y1) = self.getBounds()#find the borders of this card
            canvas.create_rectangle(x0,y0,x1,y1,fill="white")#background rect
            canvas.create_text(self.x,self.y,text = self.name)#the words on card

    def isPair(self,other):#did we click the two matching card?
        return other == self.partner#check if we picked our partner

    def __repr__(self):#return the string of the contents
        return self.name