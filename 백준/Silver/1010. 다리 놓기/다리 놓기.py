t = int(input())


def factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

for i in range(t):
    k, n = map(int ,input().split())
    anw = factorial(n)//(factorial(n-k) * factorial(k))
    print(anw)