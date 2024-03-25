from collections import deque
N,M=map(int,input().split())
degree=[0]*(N+1)
graph=[[] for i in range(N+1)]
queue=deque()

for i in range(M):
    temp=list(map(int,input().split()))
    for i in range(1,len(temp)-1):
        degree[temp[i+1]]+=1
        graph[temp[i]].append(temp[i+1])
    
ans=[]
for i in range(1,N+1):
    if(degree[i]==0):
        queue.append(i)
while queue:
    s=queue.popleft()
    ans.append(s)
    for i in graph[s]:
        degree[i]-=1
        if(degree[i]==0):
            queue.append(i)

if(len(ans)!=N):
    print(0)
else:
    for i in range(N):
        print(ans[i])
