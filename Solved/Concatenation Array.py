nums=[1,2,1]
newNums=[0 for _ in range(len(nums)*2)]
for item in range(len(nums)):
    newNums[item]=nums[item]
    newNums[item+len(nums)]=nums[item]
print(newNums)