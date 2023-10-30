arr = [37,12,28,9,100,56,80,5,12]
listOfIndex=[]
sortedArr=sorted(arr)
[listOfIndex.append(sortedArr.index(number)) for number in arr]
newList=[index+1 for index in listOfIndex]


print(newList)

