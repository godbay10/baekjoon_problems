
Three=[[1,2,3],[1,2,4],[1,5,3],[1,5,4],[6,2,3],[6,2,4],[6,5,3],[6,5,4]]

size = int(input())
diceNum = list(map(int, input().split()))

smallThree=999
smallTwo=999
smallOne=999

for i in Three:
    s=diceNum[i[0] - 1]+diceNum[i[1] - 1]+diceNum[i[2] - 1]
    if(s < smallThree):
        smallThree = s

for i in range(0,6):
    for j in range(0,6):
        if(i+j !=7 & i!=j):
            s=diceNum[i]+diceNum[j]
            if(s < smallTwo):
                smallTwo = s

sortdice = sorted(diceNum)
smallOne = sortdice[0]
print(smallTwo)
           

if(size==1):
    print(sum(diceNum)-max(diceNum))
elif(size==2):
    print(4 * smallThree + 4 * smallTwo)
else:
    print(4 * smallThree + (4 + (8 * (size-2))) * smallTwo+ (4 * (size-2) + 5*pow(size-2,2)) *smallOne)