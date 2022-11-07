hello=input("Hello! Do you want a sandwich today?(y/n)")
if hello == "y":
    sandwich = input("which samwich would you like: Chicken $5.25, Beef $6.25, tofu $5.75 (c,b,t)")
total=0
orderInformation=""
list=[c,b,t]
if sandwich=="c":
        total+=5.25
elif sandwich=="b":
        total+=6.25
elif sandwich=="t":
        total+=5.75
elif sandwich!=
orderInformation+=f"Sandwich:\t{sandwich}\n"
drink = input("You will buy a drink. (y/n)")
if drink =="y":     
        drink = input("size? s,m,l")
        if drink == "s":
            total+=1
        elif drink == "m":
            total+=1.75
        elif drink == "l":
            drink = input("would you like c?? (y,n)")
            if drink == "y":
                total+=(2.25+.38)
                drink = "c"
            else:
                total+=2.25
                drink="l"
orderInformation+=f"drink:\t{drink}\n"
fry = input("You will buy a Fry. (y/n)")
if fry =="y":
    fry=input("small,medium,large")
if fry == "small":
            total+=1
            fry="s"
elif fry == "medium":
            total+=1.55
            fry="m"
elif fry == "large":
            total+=2.00
            fry="l"
orderInformation+=f"fry:\t{fry}\n"
if sandwich!="n" and drink!="n" and fry!="n":
    print("Goodbye")
    
print(orderInformation)
print(f"subtotal={total}")
total+=total*.07
total=str(round(total,2))
#https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
print(f"total={total}")
