import random
class Generator:
    @staticmethod   #decorator
    
    def password():
        finalpassword=[]
        upperpassword=int(random.randint(2,4))
        for i in range(upperpassword):
            upperpassword=(chr(random.randint(65,90)))
            finalpassword.append(upperpassword)
        lowerpassword=int(random.randint(2,4))
        for i in range(lowerpassword):
            lowerpassword=(chr(random.randint(97,122)))
            finalpassword.append(lowerpassword)
        numberpassword=int(random.randint(2,4))
        for i in range(numberpassword):
            numberpassword=(chr(random.randint(48,57)))
            finalpassword.append(numberpassword)
        realspecialpassword="!@#$%^&*()"
        specialpassword=int(random.randint(2,4))
        for i in range(specialpassword):
            numberpassword=realspecialpassword[random.randint(0,8)]
            finalpassword.append(numberpassword)
        random.shuffle(finalpassword)
        out=""
        for i in finalpassword:
            out+=str(i)
        return out
    