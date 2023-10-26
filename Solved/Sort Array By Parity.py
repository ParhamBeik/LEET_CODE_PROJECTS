nums=[3,1,2,4]
oddList=[]
evenList=[]
[oddList.append(item) for item in nums if item%2==0]
[evenList.append(item) for item in nums if item%2==1]
newList=[oddList+evenList]
for number in newList:
    print(number)