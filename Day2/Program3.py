c=0;
d=6;
for i in range (0,4):
	s=""
	for j in range (0,c+1):
		s=s+" ";
	s=s+"*";
	for j in range (0,d):
		s=s+" ";
	s=s+"*";
	c=c+1;
	d=d-2;
	print(s)
c=c-1;
d=d+2;
for i in range (0,4):
	s=""
	for j in range (0,c+1):
		s=s+" ";
	s=s+"*";
	for j in range (0,d):
		s=s+" ";
	s=s+"*";
	c=c-1;
	d=d+2;
	print(s)
