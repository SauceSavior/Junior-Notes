class CheckInput:
    
    #check in a list
    @staticmethod   #decorator
    def getCorrectInput(listOfAnswers,question):
        userInput=""
        while not (userInput in listOfAnswers):
            userInput=input(question)
        #return True     -> you could return whatever data you need
        return userInput