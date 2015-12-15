#OregonTrail.py
import random#dictate when events happen and so forth
import tkinter#I wonder what this is for...
import sys#used to exit function
from tkinter import *

#############################
#initialization
#############################

def init(data):
    data.mode = "Start Menu"#start out at the start menu.
    data.player = Player()#create the player object, no type for now
    generateCharacters(data)#makes the default characters

def generateCharacters(data):
    data.characterList = []
    for char in range(4):#four people per party
        character = Character("",char)
        data.characterList.append(character)

##############################
#Run Function Functions
##############################


def mousePressed(event,data):
    pass

def timerFired(data):
    pass

def keyPressed(event,data):
    if data.mode == "Start Menu":
        startMenuKeyPressed(event,data)

def startMenuKeyPressed(event,data):
    if event.keysym == "1":
        data.mode = "Character Select"
        print("LINK STARTU")
    elif event.keysym == "2":
        data.mode = "Quit"

def redrawAll(canvas,data):#splits into the different redraw all functions
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    #everything is on a black background
    if data.mode == "Start Menu":
        startMenuRedrawAll(canvas,data)
    elif data.mode == "Quit":
        quitRedrawAll(canvas,data)
    elif data.mode == "Character Select":
        characterSelectRedrawAll(canvas,data)

def quitRedrawAll(canvas,data):
    #the player has left the game
    canvas.create_text(data.width/2,data.height/2,text = "CYA NERD",
                        fill = "white",font="arial 100 bold")

def startMenuRedrawAll(canvas,data):
    #title screen
    canvas.create_text(data.width/2,100,text = "Oregon 112",
                        font = "Arial 28 bold",fill = "white")#title
    canvas.create_text(data.width/2 - 100,200,text = "1.Start Game",
                        fill = "white", font =  "16",anchor = "sw")#options
    canvas.create_text(data.width/2 - 100,250,text = "2.Quit Game",fill="white",
                        font = "16",anchor = "sw")#exit the game

def characterSelectRedrawAll(canvas,data):
    #character creation screen
    for character in data.characterList:
        text = "%d. %s" % (character.index,character.name)#menu options
        canvas.create_text(data.width/2-200,100 + character.index*100,text=text,
                            fill = "white" , font = "16",anchor = "nw")
        #generates the text for the character names

#############################################
#Player/char classes
#############################################

class Player(object):
    def __init__(self):
        self.energy = 100#default is 100 energy
        self.playerType = None#default class is None until set
        self.focus = "Moderate"

    def reduceEnergy(self,amount):#reduces the players energy amount
        self.energy -= amount

    def increaseEnergy(self,amount):#replenish their energy
        self.energy += amount

class Character(object):
    def __init__(self,name,index):
        self.name = name#keeps track of the player name
        self.grade = 100#everyone starts with a 100 in the class
        self.index = index

    def reduceGrade(self,amount):#reduces the characters grade
        self.grade -= amount

    def increaseGrade(self,amount):#increases the characters grade
        self.grade += amount

    def stillPassing(self):#returns the person is still passing
        return self.getLetterGrade() != "R"
        #they're not fialing so they are passingn

    def caughtDisease(self):
        chance = random.randint(1,10000)#probability simulator
        if chance < 10:
            disease = self.pickDisease()#picks a disease at random
            return disease#return what they got hit wiht
        else:#they survived....this time
            return False

    def getLetterGrade(self):#return the letter version of grade
        if self.grade > 90:#letter grades based on numeric conversions
            return "A"
        elif self.grade > 80:
            return "B"
        elif self.grade > 70:
            return "C"
        elif self.grade > 60:
            return "D"
        else:
            return "R"

    def __repr__(self):
        return "Name = %s ; Grade = %d" % (self.name,self.grade)

    def pickDisease(self):
        return random.randomchoice(Character.diseaseList)


###################################
#Run function borrowed from 15-112 schedule
###################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    data.canvas = canvas#store the canvas
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 600)
