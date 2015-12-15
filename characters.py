#characters.py

import random

def generateCharacters(data):
    data.characterList = []
    for char in range(4):#four people per party
        character = Character("",char)
        data.characterList.append(character)

class Character(object):
    def __init__(self,name,index):
        self.name = name#keeps track of the player name
        self.grade = 100#everyone starts with a 100 in the class
        self.index = index
        self.alive = True#The character is still alive
        self.x = 650 + 50*self.index#characters are on the right third of screen
        self.y = 350#characters in bottom 2/3rds of screen
        self.headY = self.y - 30#center of chars head

    def reduceGrade(self,amount):#reduces the characters grade
        self.grade -= amount

    def increaseGrade(self,amount):#increases the characters grade
        self.grade += amount
        if self.grade >= 100:#no one gets over 100 in 112. No one.
            self.grade = 100

    def stillPassing(self):#returns the person is still passing
        if self.getLetterGrade() != "R":
            return True
        #they're not failing so they are passing
        else:#they failed
            self.alive = False#kiill this player
            return "%s dropped out of CMU" % self.name
            #ex. Anthony dropped out of cmu

    def caughtDisease(self,data):
        chance = random.randint(1,100)#probability simulator
        if chance < 40:
            disease = self.pickDisease(data)#picks a disease at random
            if disease.effect == "energy":#if it affects energy
                if data.player.energy == 0:#if there is no more energy to lose
                    self.caughtDisease(data)#call the function again
                else:
                    return disease#return what they got hit with
            return disease
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
        return "Name = %s ; Grade = %s" % (self.name,self.getLetterGrade())

    def pickDisease(self,data):#chooses what disease this character gets
        return random.choice(data.diseaseList)

    def drawCharacter(self,canvas,data):
        # canvas.create_line(640,616,660,616,fill="white")
        #draw each body part in a helper method
        self.drawBody(canvas)
        self.drawArms(canvas)
        self.drawHead(canvas)
        if data.dayHour in [4,5,6,10,11,12]:#every 3 hours
            self.drawLegsWalking(canvas)
        else:
            self.drawLegs(canvas)#draw the walking animation


    def drawBody(self,canvas):#draws the center line
        x0=x1=self.x#straight up and down line
        y0 = self.y - 20#40 units tall
        y1 = self.y + 20
        canvas.create_line(x0,y0,x1,y1,fill="white")#draws the white line

    def drawArms(self,canvas):
        y0=y1=self.y#arms are a straight horizontal line in center of body
        x0 = self.x - 10#arms are ten units long
        x1 = self.x + 10
        canvas.create_line(x0,y0,x1,y1,fill="white")

    def drawHead(self,canvas):
        x0 = self.x - 10#head is a circle of radius ten
        x1 = self.x + 10#centered on the body axis
        y0 = self.headY - 10
        y1 = self.headY + 10
        canvas.create_oval(x0,y0,x1,y1,outline="white",fill="black")

    def drawLegs(self,canvas):
        x0 = self.x#center point of the legs
        y0 = self.y + 20#legs start at the bottom of the body
        x1 = self.x - 10#end x of the left leg
        x2 = self.x + 10#end x of the right leg
        y1 = y2 = self.y + 40#left and right leg end at same vertical point
        canvas.create_line(x0,y0,x1,y1,fill="white")#draws the legs
        canvas.create_line(x0,y0,x2,y2,fill="white")

    def drawLegsWalking(self,canvas):
        x0=x1=self.x#the legs are straight up and down when taking a step
        y0 = self.y + 20
        y1 = self.y + 40
        canvas.create_line(x0,y0,x1,y1,fill="white")