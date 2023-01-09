class Information:
     
     #Constructor
     def __init__(self,fullName,userName,Password,Question):
          self.name = fullName
          self.user = userName
          self.password =Password
          self.question= Question
     #toString          
     
     #getters
     def __str__(self):
          return "Full name: "+self.name+" , "+"Username: "+self.user+" , "+"Password: "+self.password+" , "+"Security question: "+self.question
     
     def setUserName(self):
          return self.user
     
     def setPassword(self):
          return self.password
     def setQuestion(self):
          return self.question
     #setter
