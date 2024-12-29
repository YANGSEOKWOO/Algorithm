from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0<= ny < m and graph[nx][ny] and not visited[nx][ny]:
                graph[nx][ny] = graph[a][b] + 1
                visited[nx][ny] = 1
                queue.append((nx,ny))
    return graph

anw = bfs(graph,0,0)
print(anw[n-1][m-1])