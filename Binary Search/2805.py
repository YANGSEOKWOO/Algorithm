# N, M : 나무의 수, 나무의 길이
# 나무의 높이
n, m = map(int, input().split())
tree = list(map(int, input().split()))


def check(n, m):
    global tree
    cut_tree = 0
    for i in tree:
        cut_tree += max(i-n, 0)
    
    return cut_tree >= m
        

lo = 0
hi = 1000000000
while lo +1 < hi:
    mid = (lo + hi) //2
    if check(mid, m):
        lo = mid
    else:
        hi = mid
print(lo)