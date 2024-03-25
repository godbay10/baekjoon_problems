a,b,c=map(int,input().split())
dp=[]
div=[]
dp.append(b)
left=a%c
div.append(left)

def ycal(y):
    y=y//2
    if(y==0):
        return
    else:
        dp.append(y)
        ycal(y)
ycal(b)

for i in range(len(dp)-1):
    xa=dp.pop()
    xb=dp[-1]
    if(xb-2*xa==0):
        div.append(div[-1]*div[-1]%c)
    if(xb-2*xa==1):
        div.append(div[-1]*div[-1]*left%c)
print(div[-1])