d = {}
size = int(input("enter size of dictionary: "))
for i in range(size):
    k = int(input("enter key: "))
    d[k] = int(input("enter the key value: "))

sorted_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
print(sorted_d[1][1])
