from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] for _ in range(n)]

# def check():
#     for i in range(n):
#         for j in range(n):
#             print(graph[i][j], end=" ")
#         print()

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0<= ny < n and graph[nx][ny]:
                cnt +=1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return cnt
anw = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            num = bfs(i, j)
            anw.append(num)
            # check()
anw.sort()
print(len(anw))
for i in anw:
    print(i)
