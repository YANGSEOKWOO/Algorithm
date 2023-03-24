import sys
input = sys.stdin.readline

def binary_search(lo, hi):
    while (lo+1<hi):
        mid = (lo + hi)//2
        if check(mid):
            lo = mid
        else:
            hi = mid
    return lo

def check(num):
    cnt = 0
    for i in range(k):
        cnt += (lan[i]//num)
    return cnt >= n

# 왜 이분탐색인가?
# 0부터 최대값까지 임의의 정수를 기준으로 파악하기 때문에

k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))
lo = 0
hi = int(2**31)
print(binary_search(lo,hi))