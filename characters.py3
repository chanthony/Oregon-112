#characters.py

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

    def pickDisease(self):#chooses what disease this character gets
        return random.randomchoice(Character.diseaseList)