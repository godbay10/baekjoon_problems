import sys
n=int(sys.stdin.readline())
chu=list(map(int,sys.stdin.readline().split()))
m=sum(chu)
visited=[False]*(m+1)
vlist=[]

vlist.append(chu[0])
visited[chu[0]]=True

for i in range(1,len(chu)):
    temp=[]
    for j in vlist:
        if(visited[chu[i]]==False):
            visited[chu[i]]=True
            temp.append(chu[i])
        if(visited[abs(j-chu[i])]==False):
            visited[abs(j-chu[i])]=True
            temp.append(abs(j-chu[i]))
        if(j+chu[i]<=m):    
            if(visited[j+chu[i]]==False):
                visited[j+chu[i]]=True
                temp.append(j+chu[i])
    vlist+=temp

testnum=int(sys.stdin.readline())
s=list(map(int,sys.stdin.readline().split()))
for i in range(testnum):
    if s[i] in vlist:
        print("Y")
    else:
        print("N")
