import sys
input= sys.stdin.readline
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

map.sort(key = lambda x: (x[1], x[0]))
for i in map:
    print(*i)