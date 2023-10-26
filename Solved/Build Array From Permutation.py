nums = [0,2,1,5,3,4]
newNums=[0 for _ in range(len(nums))]
index=0
for item in nums:
    newNums[index]=nums[item]
    index+=1
print(newNums)
#[0,1,2,4,5,3]