#https://stackoverflow.com/questions/32317241/coin-change-maker-python-program
change=[]

x=int(input("How much change? (Whole numbers only)"))

x = x%50

x = x%25

x = x%10

x = x%5

print(x//10, "Dimes")