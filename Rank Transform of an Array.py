arr = [37,12,28,9,100,56,80,5,12]
sortedArr=sorted(arr)
#[5, 9, 12, 12, 28, 37, 56, 80, 100]
newList=[]
for item in arr:
    itemIndex=(sortedArr.index(item))+1
    newList.append(itemIndex)
    if sortedArr.count(item)==2:
        sortedArr.pop(sortedArr.index(item))
print(newList)
    

