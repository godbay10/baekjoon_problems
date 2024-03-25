import sys
def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def promising():
    sc=[]
    nc=[]
    if(cnum<=1):
        if dist(start,end)<=1000:
            print('happy')
            return
        else:
            if(cnum==0):
                print('sad')
                return
            if(dist(start,conv[0])<=1000 and dist(end,conv[0])<=1000):
                print('happy')
                return
            print('sad')
            return
    if dist(start,end)<=1000:
        print('happy')
        return
    for j in range(len(conv)):
        if(dist(start,conv[j])<=1000):
            visited[j]+=1
            sc.append(j)
        if(dist(end,conv[j])<=1000):
            visited[j]+=2
            sc.append(j)
        if(visited[j]==3):
            print('happy')
            return    
    while True:
        b=False
        for i in range(len(sc)):
            for j in range(len(conv)):
                if(dist(conv[sc[i]],conv[j])<=1000 and visited[j]==0):
                    if(visited[sc[i]]==1):
                        visited[j]+=1
                    if(visited[sc[i]]==2):
                        visited[j]+=2
                    nc.append(j)
                if(dist(conv[sc[i]],conv[j])<=1000 and visited[sc[i]]+visited[j]==3):
                    b=True
                    break
        if(b):
            print('happy')
            break
        if(len(nc)==0):
            print('sad')
            break
        sc.clear()
        sc+=nc
        nc.clear()
    return
    
t=int(sys.stdin.readline())
for i in range(t):
    conv=[]
    cnum=int(sys.stdin.readline())
    visited=[0]*cnum
    start=list(map(int,sys.stdin.readline().split()))
    for j in range(cnum):
        conv.append(list(map(int,sys.stdin.readline().split())))
    end=list(map(int,sys.stdin.readline().split()))
    promising()
    
