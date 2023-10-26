list=[1,2,3,4,5,6]
n=3
list1=[list[number] for number in range(n)]
print(list1)
list2=[list[numbers] for numbers in range(n,2*n) ]
print(list2)
wantedList=[]
for i in range(n):
    wantedList.append(list1[i])
    wantedList.append(list2[i])
print(wantedList)