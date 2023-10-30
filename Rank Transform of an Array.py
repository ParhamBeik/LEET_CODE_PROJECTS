arr = [37,12,28,9,100,56,80,5,12]
listOfIndex=[]
sortedArr=sorted(arr)
[listOfIndex.append(arr.index(number)) for number in arr]
newList=[]

for number in sortedArr:
    newList.append(arr.index(number)+1)

print(newList)

