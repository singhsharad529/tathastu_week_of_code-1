s1=int(input("Enter no of elememts in list 1: "))
l1=[]
for i in range (0,s1):
	n=input("Enter list item: ")
	l1.append(n)
l2=[]
s2=int(input("Enter no of elements in list 2: "))
for i in range (0,s2):
	n=input("Enter List Item: ")
	l2.append(n)
print("intersection of lists: ")
for i in l1:
	if i in l2:
		print(i)
