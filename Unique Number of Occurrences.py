arr = [1,3]
newList=[]
[newList.append(number) for number in arr if number not in newList]
for item in newList:
    occuranceCount=0
    for number in arr:
        if item==number:
            occuranceCount+=1
    newList[newList.index(item)]=occuranceCount

newSet=set(newList)

if len(newList)==len(newSet):
    print(True)
else:
    print(False)
    