import math 


a=int(input("1st x value."))
b=int(input("1st y value."))
c=int(input("2nd x value."))
d=int(input("2nd y value."))

x=a-c
y=b-d
distance=math.sqrt(pow(x,2)+pow(y,2))
round(distance)
#https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
print(f"Your distance: {distance}")