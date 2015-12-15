#quiz.py

class Quiz(object):
    def __init__(self,question,answers,rightAnswer):
        self.question = question
        self.answerChoices = answers
        self.rightAnswer = rightAnswer
        self.passed = False
        self.failed = True

    def quizKeyPressed(self,event,data):
        if ((event.keySym = "1") or (event.keySym = "2") or (event.keySym = "3")
            or event.keySym = "4":#if they picked an answer
            if self.isCorrect(event,data):
                self.passed = True
            else:
                self.failed = True

    def isCorrect(self,event,data):#did we pick the right answer?
        return event.keySym == self.rightAnswer

    def quizRedrawAll(self,canvas,data):
        #write the question
        canvas.create_text(500,75,text=self.question,fill="white",
                            font="Arial 16")
        for answer in range(len(self.answerChoices))