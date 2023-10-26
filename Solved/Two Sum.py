nums=[3,3]
target=6
newList=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if not (i==j) and (nums[i]+nums[j])==target:
            newList.append(i)
            newList.append(j)
    if len(newList)==2:
        break
print(newList)
