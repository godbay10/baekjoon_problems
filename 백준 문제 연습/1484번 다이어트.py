g=int(input())
b=[]
s=[]
for i in range(1,g+1):
    if g%i == 0:
        b.append(i)
for i in range(len(b)//2):
    if(b[i]+b[len(b)-i-1]) % 2 ==0:
        s.append((b[i]+b[len(b)-i-1])//2)
s.sort()
if(len(s)==0):
    print(-1)
else:
    for i in s:
        print(i)

