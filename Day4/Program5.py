n = int(input("enter no. of votes: "))
votes = []
for i in range(n):
    votes.append(input("enter the candidate which you wanna vote: "))

votes.sort()

cand = {}

for i in votes:
    if i in cand:
        cand[i]+=1
    else:
        cand[i]=1

max = 0
for i in cand:
    if cand[i]>max:
        max = cand[i]

for i in cand:
    if cand[i]==max:
        print("maximum voter candidate:",i,"with votes:",max)
