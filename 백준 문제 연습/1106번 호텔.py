"""
pNum=[9,11,4,7,2,8]
cost=[4,9,3,8,1,9]
"""

pNum=[3,5]
cost=[3,5]

person = 10
div=[0] * (6)
mCost=[0] * (6)
maxdiv = 0
place=0
totCost=0

for i in range(len(pNum)):
    div[i] = pNum[i]/cost[i]
    if(div[i] > maxdiv):
        maxdiv = div[i]
        place=i

totCost = cost[place] * (person//pNum[place])
print(totCost)
person = person % pNum[place]


