#OregonTrail.py
import random#dictate when events happen and so forth
import tkinter#I wonder what this is for...
import sys#used to exit function
import Diseases
import characters
import Quiz
from tkinter import *
from Diseases import *
from characters import *
from Quiz import *

#############################
#initialization
#############################

def init(data):
    data.mode = "Start Menu"#start out at the start menu.
    data.player = Player()#create the player object, no type for now
    generateCharacters(data)#makes the default characters
    generateDiseases(data)#initializes the diseases
    generateQuizes(data)#intializes the quizes
    data.week = 1#what week it is
    data.paused = False#whether we are paused or not
    data.showStatusScreen = False

##############################
#Run Function Functions
##############################


def mousePressed(event,data):
    pass

def timerFired(data):
    if data.paused == True:#if we're paused
        pass#do nothing
    elif not stillPlaying(data):#if we lost
        pass#add game over splash screen later
    elif data.mode == "Traveling":
        travelingTimerFired(data)

def keyPressed(event,data):
    if data.mode == "Start Menu":
        startMenuKeyPressed(event,data)
    elif data.mode == "Intro Screen":
        introScreenKeyPressed(event,data)
    elif data.mode == "Help Screen":
        helpScreenKeyPressed(event,data)
    elif data.mode == "Traveling":
        travelingKeyPressed(event, data)
    elif data.mode == "Quiz":
        quizKeyPressedHandler(event,data)
    elif data.mode == "Town":
        townKeyPressed(event, data)
    elif data.mode == "Town Help":
        townHelpKeyPressed(event, data)

def redrawAll(canvas,data):#splits into the different redraw all functions
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    #everything is on a black background
    if data.mode == "Start Menu":
        startMenuRedrawAll(canvas,data)
    elif data.mode == "Quit":
        quitRedrawAll(canvas,data)
    elif data.mode == "Character Select":
        characterSelectRedrawAll(canvas,data)
    elif data.mode == "Intro Screen":
        introScreenRedrawAll(canvas,data)
    elif data.mode == "Help Screen":
        helpScreenRedrawAll(canvas, data)
    elif data.mode == "Traveling":
        travelingRedrawAll(canvas,data)
    elif data.mode == "Quiz":
        quizDraw(canvas,data)
    elif data.mode == "Town":
        townRedrawAll(canvas, data)
    elif data.mode == "Town Help":
        townHelpRedrawAll(canvas, data)

def quitRedrawAll(canvas,data):
    #the player has left the game
    canvas.create_text(data.width/2,data.height/2,text = "CYA NERD",
                        fill = "white",font="arial 100 bold")

def stillPlaying(data):
    for character in data.characterList:
        if character.alive == True:#if any person is alive we're still going
            return True
    return False#everyone died

################################
#Start Menu
#################################

def startMenuRedrawAll(canvas,data):
    #title screen
    canvas.create_text(data.width/2,100,text = "Oregon 112",
                        font = "Arial 28 bold",fill = "white")#title
    canvas.create_text(data.width/2 - 100,200,text = "1.Start Game",
                        fill = "white", font =  "16",anchor = "sw")#options
    canvas.create_text(data.width/2 - 100,250,text = "2.Quit Game",fill="white",
                        font = "16",anchor = "sw")#exit the game

def startMenuKeyPressed(event,data):
    if event.keysym == "1":
        data.mode = "Character Select"
        characterCreation(data)
    elif event.keysym == "2":
        data.mode = "Quit"

###################################
#Character Creation mode - Not done yet gonna skip
# ###################################

# master = Tk()

# def assignNames(data):
#     for i in range(4):
#         data.characterList[i].name = data.nameList[i]
#     print(data.characterList)

# def characterCreation(data):
#     Label(master,text="Character 1").grid(row = 0)
#     Label(master,text="Character 2").grid(row = 1)
#     Label(master,text="Character 3").grid(row = 2)
#     Label(master,text="Character 4").grid(row = 3)
#     name1 = Entry(master)
#     name2 = Entry(master)
#     name3 = Entry(master)
#     name4 = Entry(master)
#     name1.grid(row=0,column=1)
#     name2.grid(row=1,column=1)
#     name3.grid(row=2,column=1)
#     name4.grid(row=3,column=1)
#     data.nameList = [name1.get(),name2.get(),name3.get(),name4.get()]
#     Button(master,text='Confirm',command=assignNames(data)).grid(row=4,column=0,)

def characterSelectRedrawAll(canvas,data):
    canvas.create_text(data.width/2,50,text="Name your study group members",
                        fill = "white",font="Arial 28")
    #character creation screen
    for character in data.characterList:
        text = "%d. %s" % (character.index + 1,character.name)#menu options
        canvas.create_text(data.width/2-200,100 + character.index*100,text=text,
                            fill = "white" , font = "16",anchor = "nw")
        #generates the text for the character names

def characterCreation(data):#generates a bunch of default names
    data.characterList[0].name = "Anthony Chan"
    data.characterList[1].name = "David Kosbie"
    data.characterList[2].name = "Joseph"
    data.characterList[3].name = "Mark Stehlik"
    data.mode = "Intro Screen"

###################################
#Intro Screen
###################################

def introScreenRedrawAll(canvas,data):#introduces the player to the game
    canvas.create_text(data.width/2,50,text="Welcome to Oregon 112",
                        fill="white",font="Arial 32 bold")
    canvas.create_text(data.width/2,150,text ="""You and your three friends \
have just arrived at CMU and have foolishly decided to register for 15-112""",
                        fill = "white",font="Arial 16")
    canvas.create_text(data.width/2,200,text="""This game will follow you and \
your friends as you go through the struggles of 112""",
                        fill = "white",font="Arial 16")
    canvas.create_text(data.width/2,data.height-50,
        text="Press enter to continue",fill="white")

def introScreenKeyPressed(event,data):
    if event.keysym == "Return":#if the user hits enter
        data.mode = "Help Screen"

##################################
#Help Screen
##################################

def helpScreenRedrawAll(canvas,data):
    canvas.create_text(data.width/2,100,text="""Each character has a grade \
which can be lowered or raised by certain events.""",fill="white",
font="Arial 16")
    canvas.create_text(data.width/2,150,text="""Be warned! If a character's \
drops to an R that character drops out of 112""",fill="white",font="Arial 16")
    canvas.create_text(data.width/2,200,text="""You also have energy which is \
shared amongst all the characters and you can spend on certain events""",
fill = "white",font = "Arial 16")
    canvas.create_text(data.width/2,250,text="""Other than that, just follow \
the onscreen instructions.""",fill = "white",font="Arial 16")
    canvas.create_text(data.width/2,400,text="""Good luck and Carpe Diem!""",
                        fill = "white",font="Arial 16")
    canvas.create_text(data.width/2,data.height-50,
                        text="Press enter to continue",fill = "white",)

def helpScreenKeyPressed(event,data):
    if event.keysym == "Return":
        data.mode = "Traveling"
        travelingInit(data)

###################################
#Traveling Mode
###################################

def travelingInit(data):#initializes the traveling mode
    data.day = 5#days to the weekend
    data.dayHour = 0#how long we've been on that day
    data.diseaseDisplayOpen = False#if the disease message box is open


def travelingRedrawAll(canvas,data):
    for character in data.characterList:
        if character.alive == True:#don't draw the dropped out members
            character.drawCharacter(canvas)
    date = "Days to the weekend: %d" % data.day#how many days are left traveling
    canvas.create_text(data.width/2,100,text = date,fill = "green",
                        font = "Arial 16")#show the date
    drawHUD(canvas, data)#draw the user hud
    if data.diseaseDisplayOpen == True:#if we need to draw the display
        drawDiseaseMessageBox(canvas, data)

def travelingTimerFired(data):
    data.dayHour += 1
    if data.dayHour == 10:
        data.charEffects = []#what has affected who today
        data.dayHour = 0#reset the counter
        data.day -= 1
        if data.day == 0:#if you made it through the week
            data.mode = "Quiz"#QUIZ TIME BABY
            return#we don't need the rest of this
        for character in data.characterList:
            if not character.alive:#if the character is dead
                pass#do nothing
            else:#DISEASE TIME BABY
                disease = character.caughtDisease(data)#pick a disease
                if disease != False:#if they actually caught something
                    disease.takeEffect(character,data.player)#catch the disease
                    data.charEffects.append(disease.showDisease(character))
                    if character.stillPassing() != True:#if this guy failed
                        data.charEffects.append(character.stillPassing())
        data.diseaseDisplayOpen = True#display the diseases for today
        data.paused = True#pause the game fam

def drawHUD(canvas,data):
    #the HUD outline
    canvas.create_rectangle(10,400,data.width-10,590,outline="green",width = 20)
    #split the HUD into two different sections
    canvas.create_line(666,400,666,600,fill="green",width=10)
    listCharacterInfo(canvas,data)
    listPlayerInfo(canvas,data)

def listPlayerInfo(canvas,data):
    weekText = "Week: %d/15" % data.week#displays what week it is
    energyText = "Energy: %d" % data.player.energy
    canvas.create_text(700,450,text = weekText,fill = "green",font = "Arial 16",
                        anchor = "nw")
    canvas.create_text(700,500,text = energyText,fill="green",
                        font="Arial 16",anchor="nw")

def listCharacterInfo(canvas,data):
    for character in data.characterList:
        y = 430 + character.index*40#vertical location of each line
        if character.alive == True:#don't list the dead guys
            canvas.create_text(40,y,text=character,fill="green",
                                font = "Arial 16",anchor = "nw")
        else:#the character is dead
            canvas.create_text(200,y,text="RIP",fill="green",font="Arial 16",
                                anchor = "nw")

def drawDiseaseMessageBox(canvas,data):#draws the disease display
    #the outline for the disease box
    canvas.create_rectangle(200,100,800,500,outline="green",fill="black",
                            width = 10)
    canvas.create_text(500,150,text="Today's Results",fill="green",
                        font="Arial 28")
    if data.charEffects != []:#if something happened today
        for effect in range(len(data.charEffects)):
            y = 200 + effect*75#stagger the effects
            #display the string of the effects of the disease
            canvas.create_text(220,y,text=data.charEffects[effect],fill="green",
                                font="Arial 16",anchor="nw")
    else:#if nothing happened
        canvas.create_text(500,300,text="Nothing happened today",fill = "green",
                            font = "Arial 18")
    canvas.create_text(500,450,text="Press enter to continue",fill = "green")

def travelingKeyPressed(event,data):
    if data.diseaseDisplayOpen:#if the display box is open
        data.diseaseDisplayOpen = False#close it
        data.paused = False#unpause

###################################
#Quiz Handlers
###################################

def quizDraw(canvas,data):
    currentQuiz = data.quizList[data.week-1]#picks the corresponding quiz
    currentQuiz.quizRedrawAll(canvas,data)

def quizKeyPressedHandler(event,data):
    currentQuiz = data.quizList[data.week-1]#picks the right quiz
    currentQuiz.quizKeyPressed(event,data)

###################################
#Towns
###################################

#goals: Notification pops up after each choice is made, class specific options

def townInit(data):#initialize the town specific data
    data.showStatusScreen = False

# def pressedDigit(event,data):
#     if event.keysym = "1":#did they press one of our choices?
#         return True
#     elif event.keysym = "2":
#         return True
#     elif event.keysym = "3":
#         return True
#     elif event.keysym = "4":
#         return True
#     elif event.keysym = "5":
#         return True
#     elif event.keysym = "6":
#         return True
#     elif event.keysym = "7":
#         return True
#     else: return False#it's not a choice they pressed
#     #note to self: alternatively make list of valid choices and check in list

def townKeyPressed(event,data):
    if event.keysym == "1" and isValidChoice(data,20):#if they picked number 1
        wentToOH(data)#take em to OH
    elif event.keysym == "2" and isValidChoice(data,10):#they studied by self
        studiedIndependently(data)
    elif event.keysym == "3" and isValidChoice(data,60):#they went ham
        data.player.energy -= 60#reduce players energy
        homeworkGrades(data,100)#adjust their grades based on 100
    elif event.keysym == "4" and isValidChoice(data,40):#the other hw choices
        data.player.energy -= 40
        homeworkGrades(data,90)
    elif event.keysym == "5" and isValidChoice(data,20):
        data.player.energy -= 20
        homeworkGrades(data,80)
    elif event.keysym == "6" and isValidChoice(data,10):
        data.player.energy -= 10
        homeworkGrades(data,60)
    elif event.keysym == "7":#they just didn't care about homework
        homeworkGrades(data,50)#don't check energy cause it costs 0
    else:
        townKeyPressed2(event,data)#part two of this function. 20 lines ftw

def townKeyPressed2(event,data):
    if event.keysym == "8":#they want to see the status
        data.showStatusScreen = True
        print(data.showStatusScreen)
    elif event.keysym == "9":
        data.mode = "Town Help"
    elif event.keysym == "Return":
        data.showStatusScreen = False

def townRedrawAll(canvas,data):
    canvas.create_text(500,30,text="Welcome to the weekend",fill="green",
                        font="Arial 28")
    canvas.create_text(300,60,text="1. Go to OH (energy - 20 ; Grade +10)",
                        fill = "green",font="Arial 16",anchor="nw")
    canvas.create_text(300,120,text="""2. Study Independently (energy -10 ; \
Grade +5)""",fill="green",font="Arial 16",anchor = "nw")
    canvas.create_text(300,180,text="""3.Go HAM on the homework (energy -60; \
Hw Grade: 100)""",fill="green",font="Arial 16",anchor = "nw")
    canvas.create_text(300,240,text="""4.Moderate effort on HW (energy -40; \
Hw Grade: 90)""",fill="green",font="Arial 16",anchor = "nw")
    canvas.create_text(300,300,text="""5.Who cares about HW?(energy -20; \
Hw Grade: 80)""",fill="green",font="Arial 16",anchor = "nw")
    canvas.create_text(300,360,text="6.What's 112?(energy -10; Hw Grade: 60)",
                        fill="green",font="Arial 16",anchor = "nw")
    canvas.create_text(300,420,text="7.**** it(energy -0; Hw Grade: 50)",
                        fill="green",font="Arial 16",anchor = "nw")
    canvas.create_text(300,480,text="8.See Status",fill="green",font="Arial 16",
                        anchor = "nw")
    townRedrawAll2(canvas,data)

def townRedrawAll2(canvas,data):
    canvas.create_text(300,540,text="9.Help",fill="green",font="Arial 16",
                        anchor = "nw")
    if data.showStatusScreen == True:#if the player wants to see the status
        drawStatusScreen(canvas,data)#draw the status

def drawStatusScreen(canvas,data):
    canvas.create_rectangle(200,100,800,500,outline="green",fill="black",
                            width=10)#the outline of the screen
    canvas.create_line(600,100,600,500,fill="green",width=5)#seperator line
    for character in data.characterList:
        y = 200 + character.index*50#vertical location of each line
        if character.alive == True:#don't list the dead guys
            canvas.create_text(240,y,text=character,fill="green",
                                font = "Arial 16",anchor = "nw")
        else:#the character is dead
            canvas.create_text(300,y,text="RIP",fill="green",font="Arial 16",
                                anchor = "nw")
    weekText = "Week: %d/15" % data.week#displays what week it is
    energyText = "Energy: %d" % data.player.energy
    canvas.create_text(640,275,text = weekText,fill = "green",font = "Arial 16",
                        anchor = "nw")
    canvas.create_text(640,325,text = energyText,fill="green",
                        font="Arial 16",anchor="nw")
    canvas.create_text(300,450,text="Press enter to escape",fill="green")

def wentToOH(data):
    data.player.energy -= 20#OH is gonna cost ya
    for character in data.characterList:
        character.grade += 10#OH boosts everyones grade by 10

def studiedIndependently(data):
    data.player.energy -= 10#studying takes 10 energy
    for character in data.characterList:
        character.grade += 5#but your grade goes up 5 points

def homeworkGrades(data,hwGrade):
    for character in data.characterList:
        if character.grade > hwGrade:#if you're above the grade
            character.grade -= 5#your grade drops
            character.stillPassing()#check to see if they failed
        elif character.grade < hwGrade:#if you're below the grade
            character.grade += 5#your grade goes up
    travelingInit(data)
    data.player.energy += 50
    data.mode = "Traveling"#doing the homework sends you forward

def isValidChoice(data,cost):#if they have enough energy for this choice
    return data.player.energy>=cost


###################################
#Town Help Screen
###################################

def townHelpRedrawAll(canvas,data):
    canvas.create_text(data.width/2,100,text="""During the weekend there are \
several different choices available for your group""",fill="white",
font="Arial 16")
    canvas.create_text(data.width/2,150,text="Here you can spend your energy to\
 boost your grade",fill="white",font="Arial 16")
    canvas.create_text(data.width/2,200,text="You can also see your grades",
    fill="white",font="Arial 16")
    canvas.create_text(data.width/2,250,text="""Once you are ready, choose a \
homework option to move on to the next week""",fill="white",font="Arial 16")
    canvas.create_text(data.width/2,300,text="""Homework grades work as \
such: every character above the homework grade goes down and 
every character below the homework grade goes up.""",
fill="white",font="Arial 16")
    canvas.create_text(data.width/2,350,text="""When you go to the next week \
you get back 50 energy.""",fill="white",font="Arial 16")
    canvas.create_text(data.width/2,550,text="Press enter to escape",
                        fill="white",font="Arial 16")

def townHelpKeyPressed(event,data):
    if event.keysym == "Return":
        data.mode = "Town"

###################################
#Player Class
###################################

class Player(object):#the general party
    def __init__(self):
        self.energy = 100#default is 100 energy
        self.playerType = None#default class is None until set
        self.focus = "Moderate"

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