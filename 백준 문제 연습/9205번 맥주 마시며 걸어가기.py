import sys
def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def promising():
    sc=[]
    nc=[]
    sc.append(start)
    while True:
        b=False
        for i in sc:
            for j in range(len(conv)):

                if(dist(i,conv[j])<=1000 and not visited[j]):
                    visited[j]=True
                    nc.append(conv[j])
            if(dist(i,end)<=1000):
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
    visited=[False]*cnum
    start=list(map(int,sys.stdin.readline().split()))
    for j in range(cnum):
        conv.append(list(map(int,sys.stdin.readline().split())))
    end=list(map(int,sys.stdin.readline().split()))
    promising()
