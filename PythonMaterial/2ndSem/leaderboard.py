


def getNames(FILENAME):
    file1=open(FILENAME,"r")
    names=[]
    for line in file1:
        index=0
        leaderName=""
        while(line[index]!=","):
            leaderName+=line[index]
            index+=1
        names.append(leaderName)
        
    return names
print(getNames("Database.txt"))

def getScores(FILENAME):
    file2=open(FILENAME,"r")
    scores=[]
    for line in file2:
        index=0
        leaderScore=""
        while(line[index]!=","):
            index+=1
        index+=1
        while(line[index]!="\n"):
            leaderScore+=line[index]
            index+=1
        scores.append(leaderScore)
        
    return scores
print(getScores("Database.txt"))


def updateLeaderboard(FILENAME,leaderNames,leaderScores,playerName,playerScore):
    index=0
    while(index<len(leaderScores)):
        if(playerScore>=int(leaderScores[index])):
            break
        else:
            index+=1
    leaderNames.insert(index,playerName)
    leaderScores.insert(index,playerScore)
    
    if(len(leaderNames)>5):
        leaderNames.pop()
        leaderScores.pop()
    file1=open(FILENAME,"w")
    for i in range(len(leaderNames)):
        file1.write(f"{leaderNames[i]},{leaderScores[i]}\n")
        
    file1.close()
    
    
#not best habits
# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  #high_scorer is a boolean to tell if the current user is a high_scorer
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()
  
  index = 0
  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while (index < len(leader_scores)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
    index = index + 1
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  #TODO:  Display message about player making the leaderboard or not
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  #TODO:  Display a gold/silver/bronze message if player earned a medal
  gold=int(leader_scores[0])
  silver=int(leader_scores[1])
  bronze=int(leader_scores[2])
  if(player_score>=gold):
       turtle_object.write("You earned a gold medal!",font=("Times New Roman",10,"bold"))
  elif(player_score>=silver):
       turtle_object.write("You earned a silver medal!",font=("Times New Roman",10,"bold"))
  elif(player_score>=bronze):
       turtle_object.write("You earned a bronze medal!",font=("Times New Roman",10,"bold"))