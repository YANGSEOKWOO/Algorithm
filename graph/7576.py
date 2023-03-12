# 보관 후 하루가 지나면, 익은 토마들의 인접한 곳에 익지않은 토마토는 영향을 받아 익는다
# 하나의 토마토의 인접은 상하좌우
# 대각선 X
# 최소 일수
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs():
    # visit[a][b] = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < n) and (0<= ny < m):
                if graph[nx][ny] == 0:
                    que.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                    # visit[nx][ny] = 1
    return 
# visit = [[0]*m for _ in range(n)]
# print(visit)
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
    print(anw_1-1)
else:
    print(-1)