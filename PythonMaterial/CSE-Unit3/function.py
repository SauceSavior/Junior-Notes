# def adding( ):
#     a=int(input("number 1"))
#     b=int(input("number 2"))
#     print(a+b)
    
# adding( )


# def ymxb():
#     m=int(input("m: "))
#     x=int(input("x: "))
#     b=int(input("b: "))
#     # print(m*x+b)
    
# for i in range(10):
#     #ymxb()
#     ymxb(1,i,4)
    
print("x | y")
print("-----")
def parabola(x): 
    return x**2+4*x+2


for i in range(6):
    print(f"{i} | {parabola(i)}")