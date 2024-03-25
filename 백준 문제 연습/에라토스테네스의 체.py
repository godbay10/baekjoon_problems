n=1000

"""
###소수 구하기 프로그램
def prime(n):
    end=int(n**0.5)
    for j in range(2, end+1):
        if(n % j ==0):
            return False
    print(n)
    return True

for i in range(2,N+1):
    prime(i)
"""

###에라토스테네스의 체
end=int(n**0.5)
primeList = [True] * (end + 1)
primeList[1] = False

for i in range(2, end + 1):
    if primeList[i]:
        if i * i > int(n ** 0.5):
            break
        for j in range(i**2, end + 1, i):
            primeList[j] = False