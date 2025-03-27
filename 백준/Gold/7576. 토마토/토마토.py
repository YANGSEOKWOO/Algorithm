from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 1: 익은 토마토, 0: 안익은 토마토, -1: 토마토X

def bfs():

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < n) and (0<= ny < m):
                if graph[nx][ny] == 0:
                    que.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    return

anw = True
anw_1 = 0
que = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i,j))
bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            anw = False
    anw_1 = max(anw_1, max(graph[i]))
if anw:
    print(anw_1 -1)
else:
    print(-1)
