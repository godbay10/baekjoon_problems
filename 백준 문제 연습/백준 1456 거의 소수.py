s, n = map(int,input().split())
start=int(s**0.5)
end=int(n**0.5)
primeList = [True] * (end + 1)
primeList[1] = False

for i in range(2, end + 1):
    if primeList[i]:
        if i * i > int(n ** 0.5):
            break
        for j in range(i**2, end + 1, i):
            primeList[j] = False


tot=0
for i in range(1, len(primeList)):
    if(primeList[i]):
        temp=i
        while True:
            temp*=i
            if(temp<=n and temp>=s):
                tot+=1
            if(temp>n):                              
                break

print(tot)
    