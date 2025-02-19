import math

n = int(input())
numbers = list(map(int, input().split()))

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
cnt = 0
for i in numbers:
    if isPrime(i):
        cnt +=1
print(cnt)