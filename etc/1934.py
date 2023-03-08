import sys
input = sys.stdin.readline


def gcd(n, m):
    if n%m == 0:
        return m
    else:
        gcd(m, n%m)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        k = gcd(a,b)
        if k:
            print
    else:
        k = gcd(a,b)

