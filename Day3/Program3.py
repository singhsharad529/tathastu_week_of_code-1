s=input("Enter a string: ")
t=""
for x in s:
	if x not in t:
		t=t+x;
print(t)
