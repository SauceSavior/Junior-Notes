orderInformation=""
total=0
sandwiches=["c","b","t"]
done=-1



stop="N"
while stop == "N"  or stop=="n":
    hello=input("Welcome to the Krusty Krab can I take your order? (Y/N)")
    if hello=="y" or hello=="Y":
        def sam():
            x=input("Would you like a sandwich, meal, or side? (S,M,O)")
            if x=="S" or x=="s":
                sandwich=input("Do you want a single Krabby Patty, a doubble Krabby Patty, or a tripple Krabby Patty. With cheese is an extra $0.25.(S,D,T,C)")
                if sandwich=="S" or sandwich=="s":
                    sandwich="Single Krabby Patty"
                    total+=1.25
                elif sandwich=="D" or sandwich=="d":
                    sandwich="Doubble Krabby Patty"
                    total+=2.00
                elif sandwich=="T" or sandwich=="t":
                    sandwich="Tripple Krabby Patty"
                    total+=3.00
                elif sandwich=="C" or sandwich=="c":
                    def cheese():
                        a=input("Single Cheese, Doubble Cheese, Tripple Cheese(S/D/T)")
                        if a=="S" or a=="s":
                            total+=1.50
                        elif a=="D" or a=="d":
                            total+=2.25
                        elif a=="T" or a=="t":
                            total+=3.25
                        else:
                            cheese()
            else:
                sam()
        orderInformation+=f"Sandwich:\t{sandwich}\n"
    # drink = input("You will buy a drink. (y/n)")
    # if drink =="y":     
    #         drink = input("size? s,m,l")
    #         if drink == "s":
    #             total+=1
    #         elif drink == "m":
    #             total+=1.75
    #         elif drink == "l":
    #             drink = input("would you like c?? (y,n)")
    #             if drink == "y":
    #                 total+=(2.25+.38)
    #                 drink = "c"
    #             else:
    #                 total+=2.25
    #                 drink="l"
    # orderInformation+=f"drink:\t{drink}\n"
    # fry = input("You will buy a Fry. (y/n)")
    # if fry =="y":
    #     fry=input("small,medium,large")
    # if fry == "small":
    #             total+=1
    #             fry="s"
    # elif fry == "medium":
    #             total+=1.55
    #             fry="m"
    # elif fry == "large":
    #             total+=2.00
    #             fry="l"
    # orderInformation+=f"fry:\t{fry}\n"


    # stop=input("Will that be all today?(Y/N)")
    

    
        
print(orderInformation)
print(f"subtotal={total}")
total+=total*.07
total=str(round(total,2))
#https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
print(f"total={total}")