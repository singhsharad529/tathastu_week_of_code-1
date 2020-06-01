s=int(input("Enter no of elememts in list: "))
li=[]
for i in range (0,s):
	n=input("Enter list item: ")
	li.append(n)
l=[]
for i in li:
	if i not in l:
		l.append(i)
print(l)
