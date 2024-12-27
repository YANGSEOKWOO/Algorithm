import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 기존의 코드에서는 graph를 2차원 배열
# 각 인덱스 => 연관된 노드로 생각했었음
# 이 경우는 어떻게 할지?
def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx <n and 0<= ny < m:
                if not graph[nx][ny]:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
def check(graph):
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=" ")
        print()

# example 
"""
4 5
00110
00011
11111
00000
"""
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
print(graph)

cnt = 0
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            bfs(graph, i, j)
            print('-------------------------')
            check(graph)
            cnt += 1



print(cnt)