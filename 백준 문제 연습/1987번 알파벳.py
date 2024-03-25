N,M=map(int, input().split())
board=[list(input()) for _ in range(N)]
vAlpha=[False]*26
move=[[1,0],[0,1],[-1,0],[0,-1]]
vAlpha[ord(board[0][0])-65]=True
tot=0
gtot=1

def out(x,y):
    if(0<=x<N and 0<=y<M):
        return False
    return True
    

def bfs(x,y):
    global gtot
    global tot
    for i in range(len(move)):
        mx=x+move[i][0]
        my=y+move[i][1]
        if(not out(mx,my)):
            if(vAlpha[ord(board[mx][my])-65]):
                if(gtot>tot):
                    tot=gtot
            else:
                vAlpha[ord(board[mx][my])-65]=True
                gtot+=1
                bfs(mx,my)
                vAlpha[ord(board[mx][my])-65]=False
                gtot-=1

if(N==1 and M==1):
    print(1)
else:
    bfs(0,0)
    print(tot)