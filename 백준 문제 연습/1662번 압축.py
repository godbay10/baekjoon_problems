a=input(str())
queue=[]
mstack=[]
queue.append(0)
prenum=0
tot=0

for i in range(len(a)):
    if(ord(a[i])>=48 and ord(a[i])<=57):
        queue[-1]+=1
        prenum = ord(a[i])-48
    if(a[i]=='('):
        queue[-1]-=1
        mstack.append(prenum)
        queue.append(0)
    if(a[i]==')'):
        tot=mstack.pop()*queue.pop()
        queue[-1]+=tot

print(queue.pop())
