class Student:

    def __init__(self,first,last):
        self.firstName = first
        self.lastName = last
        self.courses=[]
    
    
    def __str__(self):
        out=f"{self.lastName},{self.firstName}\n"
        for c in self.courses:
            out+=f"\t{c}\n"
        return out
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def addCourse(self,newCourse):
        self.courses.append(newCourse)
        