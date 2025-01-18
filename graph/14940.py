from collections import deque

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
anw = [[0]*m for _ in range(n)]

# 각 지점에서 목표 지점까지의 거리

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    anw[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] ==1:
                anw[nx][ny] = anw[a][b] + 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return

for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            bfs(x,y)
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and visited[x][y] == 0:
            print(-1, end=" ")
        else:
            print(anw[x][y], end=" ")
    print()
