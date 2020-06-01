def per(List, String = ""):
    Set = set(List)
    strList = []
    if len(Set) == 1:
        String += "".join(List)
        return list([String])
    for x in Set:
        List1 = list(List)
        S = String + x
        List1.remove(x)
        strList.extend(permutation(List1, S))
    return strList

string = input("Enter a string: ")
List = per(list(string))
print("All the permutation of given string is: " + ", ".join(List))
