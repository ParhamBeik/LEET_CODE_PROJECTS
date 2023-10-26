strs = ["dog","racecar","car"]
myList=[]
for character in strs:
    for char in character:
        myList.append(char)
newList=""
for item in myList:
    if myList.count(item)>=len(strs) and item not in newList:
        newList+=item
print(newList)
