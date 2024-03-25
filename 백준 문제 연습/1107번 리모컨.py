N=250000
x = 65555
a = [6,5,5,5,5]

ban=[0,5,6,9]
able=[1,2,3,4,7,8]
startnum=0

def BFChannel():
    num=[]
    for i in range(0,N):
        num = list(str(x+i))
        for j in num:
            for k in ban:
                if(int(j)==k):
                    break
        if(j==len(num)-1 & k==len(ban)-1):
            print(num)


def OrChannel():
    return abs(x - 100)

print(min(BFChannel(),OrChannel()))