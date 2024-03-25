"""
crane=[11,17,5,2,20,7,5,5,20]
box=[18,18,15,15,17]
"""
cNum = int(input())
crane = []
crane = list(map(int,input().split()))
bNum = int(input())
box = []
box = list(map(int,input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)


tot = 0
if(box[0] > crane[0]):
    print(-1)
else:
    while box:
        tot+=1
        cnum = 0
        a = []
        for k in range(len(box)):
            if(cnum == len(crane) or cnum==len(box)):
                for t in a:
                    box.remove(t)
                a.clear()
                break
            if(box[k] <= crane[cnum]):
                a.append(box[k])
                cnum+=1
        if(len(a) != 0):
            for t in a:
               box.remove(t)
    print(tot)