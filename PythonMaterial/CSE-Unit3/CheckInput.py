class CheckInput:
    
    ui="Yes"
    def getCorrectInput(userInput,listOfAnswers,question):
        while not (userInput in listOfAnswers):
            userInput=input(question)
        return True      
        return userInput