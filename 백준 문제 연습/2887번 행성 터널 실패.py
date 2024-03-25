N=int(input())
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
parent=[j for j in range(N)]
data=[0 for i in range(N)]
totcost=0

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


def umin(x):
    orr=arr[x]
    opp=[]
    for i in range(len(arr)):
        if(i!=x):
            opp+=arr[i]
    s=-1
    e=-1
    mini=2000000000
    for i in orr:
        for j in opp:
            if(cal(i,j)<mini):
                s=i
                e=j
                mini=cal(i,j)
    return [s,e,mini]
    
tt=[]
arr=[]
while True:
    tt.clear()
    arr.clear()
    for i in range(len(parent)):
        if find(parent[i]) not in tt:
            tt.append(find(parent[i]))
            arr.append([i])
        else:
            arr[tt.index(find(parent[i]))]+=[i]
    pnum=len(tt)
    if(pnum==1):
        break
    data=[]
    for i in range(pnum):
        es=umin(i)
        if(find(es[0])!=find(es[1])):
            union(es[0],es[1])
            totcost+=es[2]
print(totcost)