import sys
input = sys.stdin.readline

def gcd(n,m):
    while m>0:
        n, m = m, n% m
    return n

a, b = map(int, input().split())
print("1" * gcd(a,b))