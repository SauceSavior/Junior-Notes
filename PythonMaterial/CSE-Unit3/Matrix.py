import random

while(True):
    out=" "
    i=0
    while(i<=4250):
        out+=chr(random.randint(32,126))
        i+=1
        color(0,32)
    print(out)
