left=0

height=int(input()) #allows for a height

for h in range(height): #Sets a height for the triangle
    left+=1
    
right=0

for h in range(height):
    right+=1 
    print(""*int(height-right), end="") #Fixes spacing
    
    
for h in range(height):
    counter=0
for h in range(height): #for the height increase the amount of #
    counter+=1
    print(" "*int(height-counter), end="")
    print("#"*int(counter,end='')) #prints #
    print("#"*int(counter),end="\n") #makes next line of #
#credit to zander for helping me out

