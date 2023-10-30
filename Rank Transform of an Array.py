arr = [37,12,28,9,100,56,80,5,12]
listOfIndex=[]
sortedArr=sorted(arr)
[listOfIndex.append(sortedArr.index(number)+1) for number in arr]
print(newList)

