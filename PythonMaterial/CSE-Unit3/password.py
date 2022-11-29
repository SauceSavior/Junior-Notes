import random
import string
z=0
d=0
done="N"
while z != 1:
    if done == "y" or done =="Y":
        print("Thanks for using me!")
        z+=1
    else:
        x=int(input("How many digits?"))
        final=''.join(random.choice(string.digits) for i in range(x))
        a=int(input("How many uppercase?"))
        final+=''.join(random.choice(string.ascii_uppercase) for i in range(a))
        b=int(input("How many lowercase?"))
        final+=''.join(random.choice(string.ascii_lowercase) for i in range(b))
        y=["!","@","#","$","%","^","&","*","(",")"]
        c=int(input("How many special stuffs"))
        while d!=c:
            final+=''.join(random.choice(y))
            d+=1
        #https://pynative.com/python-generate-random-string/
        final=''.join(random.sample(final,len(final)))
        print(final)
        done=input("Are you done? (Y/N)")