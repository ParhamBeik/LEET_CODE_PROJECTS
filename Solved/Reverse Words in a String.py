s = "Let's take LeetCode contest"
newS=""
for item in s[::-1]:
    newS+=item
newList=newS.split(" ")
newNewList=""
for item in newList[::-1]:
    newNewList+=item
    newNewList+=" "
print(newNewList)
