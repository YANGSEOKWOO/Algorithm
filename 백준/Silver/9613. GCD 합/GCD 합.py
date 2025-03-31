
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

t = int(input())

for i in range(t):
    n, *gcd_list = map(int, input().split())

    gcd_num = 0
    for j in range(n-1):
        for k in range(j+1, n):
            gcd_num += gcd(gcd_list[j], gcd_list[k])
    print(gcd_num)
