arr = [40,10,20,30]
listOfIndex=[]
sortedArr=sorted(arr)
[listOfIndex.append(sortedArr.index(number)) for number in arr]
newList=[index+1 for index in listOfIndex]


print(newList)

