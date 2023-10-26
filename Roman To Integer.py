s = "MCMXCIV"
sum=0
for item in s:
    if item=="I":
        sum+=1   
    elif item=="V":
        sum+=5
    elif item=="X":
        sum+=10
    elif item=="L":
        sum+=50
    elif item=="C":
        sum+=100
    elif item=="D":
        sum+=500
    elif item=="M":
        sum+=1000

print(sum)
    