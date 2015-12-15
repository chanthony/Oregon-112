#quiz.py

import random
import QuizX
from QuizX import *

def generateQuizes(data):#generates the quiz and adds it to the lsit
    data.quizList = []#the list of quizes is empty
    data.quizList.append(Quiz("What room number is the Rashid Auditorium?",
                        ["4401","4410","4420","Not Here"],"1"))#week1
    data.quizList.append(Quiz("Which of these is not a loop used in 15-112?",
                        ["For loop","While loop","Iterative loop",
                        "Recursive loop"],"3"))#week2
    data.quizList.append(Quiz("How many characters is \"\\t\" ",
                                ["1","2","3","Undefined"],"1"))#week3
    data.quizList.append(Quiz("""Which of the following will turn the list a = \
[-2,1,4] into [1,-2,4]?""",["sort(a)","sort(abs(a))",
"sort(-a)","sort(a,key=abs)"],"4"))#week4
    data.quizList.append(Quiz("""What is the term for a 2D list with items of \
different lengths?""",["non-symmetric","ragged","uneven","dumb"],"2"))#week5
    data.quizList.append(Quiz("Which of the following creates and empty set?",
["{}","set({})","set()","None of the above"],"3"))#week6
    data.quizList.append(Quiz("""Which of the following is not a valid tkinter \
shape?""",["circle","polygon","rectangle","line"],"1"))#week7
    data.quizList.append(Quiz("MIDTERM #1",["yes","no","42","vjcourfxoasscl"],
                        "3"))#week8
    generateQuizes2(data)#DARN YOU 20 line limittttttttt

def generateQuizes2(data):
    data.quizList.append(Quiz("""What is the term for a function defined within\
 a class?""",["function","method","helper function","a function within a class"]
, "2"))#WEEK9 BABY
    data.quizList.append(Quiz("""What is the term for the list of recursive \
calls made by a function?""",
["Recursive Stack","Recursive depth","Recursive path","Call stack"],"4"))#week10
    data.quizList.append(Quiz("""If b is an instane of a subclass of A, which of\
the following returns True?""",
["isInstance(b,A)","type(b)==A","b==A","All of the above"],"1"))#week 11
    data.quizList.append(Quiz("""Who of the following does not teach a 112 \
recitation?""",["Rebecca Stokes","Josh Korn","Rohan Varma","Julia Yang"],"3"))
    data.quizList.append(Quiz("Turkey?",["Gobble","Gobble","Gobble","Gobble"],
                            "3"))#week13 - THANKSGIVING FAM
    data.quizList.append(Quiz("When are David Kosbie's office hours?",
["Sat/Sun 2pm - 10pm","Tue/Thurs 12pm - 2pm","Wed/Fri 10:30am - 12:30pm",
"None of the above"],"2"))#week14
    data.quizList.append(Quiz("P = NP?",["yes","no","Can't be proven","nes"],
                                ""))

class Quiz(object):
    def __init__(self,question,answers,rightAnswer):
        self.question = question#stores the various info
        self.answerChoices = answers
        self.rightAnswer = rightAnswer
        self.passed = False#they haven't passed yet
        self.failed = False#they haven't failed yet

    def quizKeyPressed(self,event,data):
        if ((event.keysym == "1") or (event.keysym == "2") or
            (event.keysym == "3") or event.keysym=="4"):#if they picked a answer
            if self.passed == True or self.failed == True:
                pass 
            elif self.isCorrect(event,data):
                self.passed = True#we passed!
            else:
                self.failed = True#oops. Guess we are dumb
        elif event.keysym == "Return":
            if self.passed == True or self.failed == True:#if results are up
                self.modeTransition(data)
                data.week += 1#we're on the next week
                if data.week > 15:#if we finished all the weeks
                    for character in data.characterList:
                        if character.alive == True:#if at least one made it
                            data.mode = "Victory"#go to the victory screen
                            return
                    data.mode = "Failure"#no one made it so we lost

    def modeTransition(self,data):#move on after the quiz
        chance = random.randint(0,100)
        if chance <= 20:#1/5 chance
            data.mode = "QuizX"#go to a quizX
            generateQuizX(data)#write the quiz
        else:
            data.showEventScreen = False
            data.showStatusScreen = False
            data.mode = "Town"#go to the weekend like normal

    def isCorrect(self,event,data):#did we pick the right answer?
        if event.keysym == self.rightAnswer:#we got it right!
            for character in data.characterList:#everyone gets five points
                character.grade += 10#
            return True
        else:#YOU ARE WRONG SIR
            for character in data.characterList:#everyone loses five points
                character.grade -= 10#you must be punished for you errors

    def quizRedrawAll(self,canvas,data):
        #write the question
        canvas.create_text(500,50,text="IT'S QUIZ TIME",fill="green",
                            font="System 28")
        canvas.create_text(500,100,text=self.question,fill="green",
                            font="System 17")
        for answer in range(len(self.answerChoices)):#write up the answer choice
            y = 175 + 100*answer#each answer is 100 units apart
            answerChoice = "%d. %s" % (answer+1,self.answerChoices[answer])
            #ex. "1. Banana"
            canvas.create_text(50,y,text=answerChoice,fill="green",
                                font="System 17",anchor="nw")
        if self.passed == True or self.failed == True:#if we picked an answer
            self.drawResultsBox(canvas,data)#draw a result box
        text = "Press a number to choose that option"
        canvas.create_text(data.width/2,data.height - 70,text=text,fill="green",
                        font="System 18") 

    def drawResultsBox(self,canvas,data):  
            if self.passed == True:#if we already passed
                result = "passed"#passed or failed
                change = "goes up"#grade goes up or down
            else:#we failed
                result = "failed"
                change = "drops"
            overallResult="You %s!" % result
            #"You failed" or "you passed"
            gradeImpact = "Everyone's grade %s 10 points" % change
            #"Everyones grade goes up 5 points or everyones grade goes down 5"
            canvas.create_rectangle(200,200,800,400,outline="green",
                                    fill="black",width=10)#draw a results box
            canvas.create_text(500,275,text=overallResult,fill="green",
                                font="Arial 16")
            canvas.create_text(500,325,text=gradeImpact,
                                fill="green",font="Arial 16")
            canvas.create_text(500,350,text="Press enter to continue",
                                fill="green")