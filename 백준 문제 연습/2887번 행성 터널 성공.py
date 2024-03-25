import heapq
N=int(input())
planets=[0]*N
parent=[j for j in range(N)]
for i in range(N):
    x, y, z = map(int, input().split())
    planets[i] = (x, y, z, i)

xsort = sorted(planets, key=lambda x: x[0]) 
ysort = sorted(planets, key=lambda x: x[1])  
zsort = sorted(planets, key=lambda x: x[2])

tt=[]
for i in range(N-1):
    heapq.heappush(tt, (abs(xsort[i][0]-xsort[i+1][0]),xsort[i][3],xsort[i+1][3]))
    heapq.heappush(tt, (abs(ysort[i][1]-ysort[i+1][1]),ysort[i][3],ysort[i+1][3]))
    heapq.heappush(tt, (abs(zsort[i][2]-zsort[i+1][2]),zsort[i][3],zsort[i+1][3]))

def cal(x,y):
    return min(abs(a[x][0]-a[y][0]),abs(a[x][1]-a[y][1]),abs(a[x][2]-a[y][2]))


def find(x):
	if (parent[x] == x):
		return x
	return find(parent[x])

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

totcost=0
line=0
while line<N-1:
    c,s,e = heapq.heappop(tt)
    if find(s)!=find(e):
        union(s,e)
        totcost+=c
        line+=1
print(totcost)