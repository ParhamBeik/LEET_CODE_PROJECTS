nums = [3,4,5,2]
firstMaxNumber=max(nums)
nums.pop(nums.index(firstMaxNumber))
secondMaxNUmber=max(nums)
print(firstMaxNumber-1)*(secondMaxNUmber-1)
