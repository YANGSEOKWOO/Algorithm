import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    member = []
    for i in range(n):
        member.append(list(map(int, input().split())))
    member.sort()
    cnt = 1
    min_val = member[0][1]
    for j in range(1,n):
        if member[j][1] < min_val:
            cnt += 1
            min_val = member[j][1]
    print(cnt)

