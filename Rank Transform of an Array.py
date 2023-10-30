arr = [37,12,28,9,100,56,80,5,12]
listOfIndex=[]
sortedArr=sorted(arr)
[listOfIndex.append(sortedArr.index(number)+1) for number in arr]
listOfRanksSimilar=[]
[listOfRanksSimilar.append(number) for number in listOfIndex if listOfIndex.count(number)>=2 and number not in listOfRanksSimilar]
for number in listOfIndex:
    if number>listOfRanksSimilar[0]:
        listOfIndex[listOfIndex.index(number)]=number-1
print(listOfRanksSimilar)
print(listOfIndex)

