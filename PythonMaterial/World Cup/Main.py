from Team import Team



teams=[]
for n in ['Netherlands','England','Poland','France','Spain','Croatia','Brazil','Portugal']:
    teams.append(Team(n,0,0,0))

day1Wins=[1,0,1,1,0,1,0,0]


for t in teams:
    print(t)
for i in range(len(day1Wins)):
    if day1Wins[1]==1:
        teams[i].addWins()
print()
for t in teams:
    print(t.overAllStats())

# k=0
# for team in teams:
#     print(f"{team} has {scores[k]} many points")
#     k+=1
    
# for i in range(len(teams)):
#     print(f"{teams[i]} has {scores[i]} many points")
# print()
# for i in range(len(injuries)):
#     print(f"{teams[i]} has {injuries[i]} injuries")
# print()
# for i in range(len(wins)):
#     print(f"{teams[i]} has {wins[i]} wins")
# print()
        