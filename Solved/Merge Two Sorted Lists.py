list1 = [1,2,4]
list2 = [1,3,4]
myList=[]
[myList.append(number) for number in list1]
[myList.append(number) for number in list2]
print(sorted(myList))