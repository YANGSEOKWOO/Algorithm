# 집터 내 의 땅 높이를 일정하게 바꾸기
'''
1. 좌표 (i,j)위의 블록을 제거하여 인벤토리에 넣기 - 2초
2. 인벤토리에서 블록 하나를 꺼내어 좌표(i,j)의 가장 위의 블록 - 1초

초반 인벤토리 블록 수 : b
'''
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

max_value = max(max(row) for row in ground)
min_value = min(min(row) for row in ground)
min_time = 1e9
max_height = 0
for target in range(min_value, max_value+1):
    toSub = 0
    toAdd = 0
    for i in range(n):
        for j in range(m):
            if target > ground[i][j]:
                toAdd += target- ground[i][j]
            elif target < ground[i][j]:
                toSub += ground[i][j] - target
    if (toAdd -b) > toSub:
        break
    else:
        time = toSub*2 + toAdd
        if time <= min_time:
            min_time = time
            max_height = target
print(min_time, max_height)
