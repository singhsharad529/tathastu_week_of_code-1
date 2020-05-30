r=[eval(x) for x in input("Enter runs in 60 balls for 3 players seperated by comma").split(",")]
print(r)
sr=[x*100/60 for x in r]
print("Strike rate of the players is",sr)
r2=[x*2 for x in r]
print("If players played 60 balls more then their score is ",r2)
s=[int(x/6) for x in r]
print("Max number of sixes by players in 60 balls",s)
