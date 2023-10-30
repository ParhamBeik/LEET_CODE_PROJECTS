arr = [40,10,20,30]
listOfIndex=[]
sortedArr=sorted(arr)
[listOfIndex.append(arr.index(number)) for number in arr]
newList=[]

for number in sortedArr:
    newList.append(arr.index(number)+1)

print(newList)

