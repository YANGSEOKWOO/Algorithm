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
        print(gcd(a,b))
    else:
        print(gcd(b,a))

