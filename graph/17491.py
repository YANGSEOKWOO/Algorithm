from collections import deque
import sys
input = sys.stdin.readline

# 거리를 두번 구해야함

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
n= int(input())
graph = [ [0]*(n+1)for _ in range(n+1)]


for i in range(n):
    a, b= map(int, input().split())
    graph[a][b] = 1

temp = []
# for i in range(n):
#     print()
#     for j in range(n):
#         print(graph[i][j], end="")


def bfs(a,b):
    graph[a][b] = 0
    q = deque()
    q.append((a,b))
    cnt += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if n>nx>=0 and n>ny>=0:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
                    temp.append([nx, ny])
    

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)