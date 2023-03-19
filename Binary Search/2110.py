import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for i in range(n)]
home.sort()
lo = -1
hi = 1000000001

def check(num):
    cnt = 1
    current = home[0]
    for i in range(1, len(home)):
        if home[i] >= current + num:
            cnt += 1
            current = home[i]
    return cnt >=c


while(lo+1<hi):
    mid = (lo+hi)//2
    if check(mid):
        lo = mid
    else:
        hi = mid
print(lo)