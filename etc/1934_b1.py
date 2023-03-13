import sys
input = sys.stdin.readline

def gcd(n,m):
    while m>0:
        n, m = m, n% m
    return n

def lcm(n, m):
    return n*m//gcd(n,m)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a >b:
        print(lcm(a,b))
    else:
        print(lcm(b,a))