secret=52

ui=int(input("guess a number 0-100"))

while(not ui.isdigit()):
    ui=(input("guess a number 0-100"))
ui=int(ui)
while(secret!= ui):
    if secret < ui:
        print("to high")
    elif secret > ui:
        print("to low")
    ui=int(input("guess a number 0-100"))
print("You got it")