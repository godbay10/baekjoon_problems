from collections import deque
tnum=int(input())
rnum=int(input())
toy=[[] for j in range(tnum)]
ing=[[] for j in range(tnum)]
for i in range(rnum):
    n,f,s=map(int,input().split())
    toy[n-1].append([f-1,s])
    ing[n-1].append(f-1)

default=[]
queue=deque()
order=[]
visited=[False]*tnum
for i in range(tnum):
    if(len(toy[i])==0):
        default.append(i)
        queue.append(i)
        visited[i]=True
        
while True:
    if not queue:
        
        break
    while queue:
        n=queue.popleft()
        order.append(n)
        for i in range(tnum):
            for j in ing[i]:
                if(j==n):
                    ing[i].remove(n)
    for i in range(tnum):
        if(len(ing[i])==0 and visited[i]==False):
            queue.append(i)
            visited[i]=True

temp=[]
for i in order:
    temp.append(toy[i])
toy=temp
make=[[0 for _ in range(len(default))] for _ in range(tnum)]
for i in range(len(default)):
      make[i][i]=1
for i in range(tnum):
    if(len(toy[i])!=0):
        for j in toy[i]:
            s=0
            for k in make[order.index(j[0])]:
                make[i][s]+=k*j[1]
                s+=1
for i in range(len(default)):
    if(make[-1][i]!=0):
        print(order[i]+1, make[-1][i])
            
