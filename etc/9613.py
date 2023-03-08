import sys
input = sys.stdin.readline

n = int(input())


def gcd(n,m):
    while m> 0:
        n, m = m, n % m
    return n

for i in range(n):
    anw = 0
    num = list(map(int, input().split()))
    k = num.pop(0)
    for i in range(k-1):
        for j in range(i+1,k):
            if num[i] > num[j]:
                anw += gcd(num[i],num[j])
            else:
                anw += gcd(num[j], num[i])
    print(anw)