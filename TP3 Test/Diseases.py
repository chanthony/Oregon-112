#diseases.txt

def generateDiseases(data):
    diseaseList = []#keep the diseases as a list
    diseaseList.append(Disease("performed a ritual sacrifice to the 112 gods",
                                "grade",10))#generate each disease and store it
    diseaseList.append(Disease("forgot to backup their work and lost it",
                                "grade",-10))
    diseaseList.append(Disease("angered the great Kosbie","grade",-20))
    diseaseList.append(Disease("""forgot a parentheses in their code and spent
15 hours looking for it""","grade",-5))
    diseaseList.append(Disease("""watched a Youtube video that had the word 
programming in the title""","grade",5))
    diseaseList.append(Disease("caught dysentery","energy",-50))
    diseaseList.append(Disease("got dumped","energy",-30))
    diseaseList.append(Disease("hung out with their friends","energy",20))
    diseaseList.append(Disease("told a funny joke","energy",10))
    diseaseList.append(Disease("had their interp class cancelled","energy",40))
    data.diseaseList = diseaseList#store the list

class Disease(object):#the various effects
    def __init__(self,name,effect,amount):
        self.name = name#not the name but what the disease is
        self.effect = effect#what the disease effects
        self.amount = amount#the size of the impact
        if self.amount < 0:#if negative
            self.change = "lost"#whether we lost or gained amount
        else:#positive
            self.change = "gained"

    def takeEffect(self,char,player):
        if self.effect == "energy":#if the energy is hurt
            player.energy += self.amount#change the energy
            if player.energy < 0:#if at negative energy
                player.energy = 0#set us back at 0
            elif player.energy >= 100:#cap energy to 100
                player.energy = 100
        elif self.effect == "grade":
            char.grade += self.amount
        else:    
            #we clearly havent' coded this yet so let me know
            raise NameError("This disease effect has not been coded yet!")

    def showDisease(self,char):#shows the disease dialogue
        if self.effect == "energy":
            line = "%s %s.\n" % (char.name,self.name)
            #ex. You forgot your homework
            line += "Your group %s %d energy." % (self.change,abs(self.amount))
        else:#if it's something other than energy
            line = "%s %s. \n" % (char.name , self.name)
            #ex. Jimmy forgot to close his parentheses
            line += "%s %s %d %s points" % (char.name,self.change,
                                            abs(self.amount),self.effect)
            #ex. Jimmy gained 15 energy
        return line