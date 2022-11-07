from token import NEWLINE

event=["Welcome adventurer! You are on a quest to explore the no mans land of the forest...I think i wasnt really paying attion to the quest board. If you could do that for me that would be great. Thanks adventurer i apperciate it happy hunting! (ps: dont forget to use y/n when answering)","As you travel down the path you find a fork in the road...(How origional right?)","As you make it through the clearing you think to yourself you have been here before... The same fork in the road."
,"As you travel you find a crate.","",5,6,7,8,9,10,11,12,13]



loop=0
def death1():
    global loop
    print(event[2])
    input("Do you wish to go left?")
    loop+=1
    if loop!=10:
        death1()
    else:
        print("You died adventurer... You had a good run well not really but please try again.")
        start()

def start():
        print(event[0])
        s=input("Do you wish to start?")
        if s=="y":
            event[2]
        else: 
            start() #loops the welcome if they decide to not start


start()

print(event[1])
ui=input("Do you wish to go left?")
if ui=="y":
        print(event[3])
else: 
        death1()
        
print(event[4])
ui1=input("Do you wish to open the crate?")
if ui1=="y":
    print(event[5])
elif ui1=="n":
    print(event[6])


