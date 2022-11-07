# import random

# def giveMeSomeNumbers():
#     someNumbers=[]
#     for i in range(10):
#         somenumbers.append(random.randint(24,69))
#         return someNumbers
    
# randomListOfNumbers=giveMeSomeNumbers(10,24,69)
# print(randomListOfNumbers)
# randomListOfNumbers=giveMeSomeNumbers(10000,-100000,100000000000)
# print(randomListOfNumbers)

import random 
from conversion import *
menu='''
in to cm (ic)
cm to in (ci)
kg tog (kgg)
g to kg (gkg)
which conversion?
'''
user=input(menu)
while(user!="quit"):
    if user=="ic":
        in2cm()
    elif user=="ci":
        cm2in()
    elif user=="kgg":
        kg2g()
    elif user=="gkg":
        g2kg()
    
    
    user=input(menu)
