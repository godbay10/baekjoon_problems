N=int(input())
dp=[[99 for j in range(N)]for i in range(N)]
for i in range(N):
    dp[i][i]=0

def union(x,y):
    dp[x][y]=1
    dp[y][x]=1
    for i in range(N):
        for j in range(N):
            if(dp[i][j]>dp[i][x]+dp[x][j]):
                dp[i][j]=dp[i][x]+dp[x][j]
                dp[j][i]=dp[i][x]+dp[x][j]
            if(dp[i][j]>dp[i][y]+dp[y][j]):
                dp[i][j]=dp[i][y]+dp[y][j]
                dp[j][i]=dp[i][y]+dp[y][j]
 
def cal():
    marr=[]
    parr=[]
    for i in range(N):
        marr.append(max(dp[i]))
    for i in range(N):
        if(min(marr) == marr[i]):
            parr.append(i+1)
    print(min(marr), len(parr))
    for i in parr:
        print(i, end = " ")
        
while True:
    a, b = map(int,input().split())
    if a==-1 and b==-1:
        break
    union(a-1,b-1)
cal()