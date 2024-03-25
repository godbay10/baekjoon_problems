from collections import deque
M,N=map(int,input().split())
board=[[0 for j in range(M)] for i in range(N)]
queue=deque()
dir=[[0,1],[0,-1],[1,0],[-1,0]]
visited=[[False for j in range(M)] for i in range(N)]
for i in range(N):
    board[i]=list(map(int, input().split()))

def out(x,y):
    if(0<=x<N and 0<=y<M):
        if(board[x][y]!=-1 and visited[x][y]==False):
            return False
    return True

def bfs(a,b,t,queue):
    for i in range(4):
        x=a+dir[i][0]
        y=b+dir[i][1]
        if(not out(x,y)):
            visited[x][y]=True
            queue.append([x,y,t+1])

def ans(tot):
    for i in range(N):
        for j in range(M):
            if(board[i][j]!=-1 and visited[i][j]==False):
                return -1
    return tot

for i in range(N):
    for j in range(M):
        if(board[i][j]==1):
            visited[i][j]=True
            queue.append([i,j,0])

tot=0
while queue:
    a,b,t=queue.popleft()
    bfs(a,b,t,queue)
    tot=t
    
print(ans(tot))
