from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
max_reach = []

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        cnt = 1
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m:
                if nx == n-1 and ny == m-1:
                    max_reach.append(cnt)
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    queue.append((nx,ny))
bfs(graph,0,0)
print(max_reach)