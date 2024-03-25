
group=[]

k=1

a=int(input())
for i in range(0,10):
    group.append(i)

while(k<10):
    for i in range (1,10):
        for j in range(0, len(group)):
            if(len(str(group[j])) == k):
                if(k==1):
                    if(i > group[j]):
                        group.append(i*pow(10,k)+group[j])
                else:
                    if(i > group[j]//pow(10,k-1)):
                        group.append(i*pow(10,k)+group[j])
    k+=1

if a >= len(group):
	print(-1)
else:
	print(group[a])


"""
while(k<10):
    for i in range (1,10):
        for j in range(0, len(group)):
            if(i > group[j]):
                newgroup.append(i*pow(10,k)+group[j])
    group.clear()
    group=newgroup
    k+=1

for i in group:
    print(i)
    
a=int(input())
print(group[a])
"""




