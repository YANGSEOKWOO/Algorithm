from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, graph):
    queue = deque()
    queue.append((x,y))
    cnt = 1

    graph[x][y] = -1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = -1
                cnt += 1
                queue.append((nx, ny))
    return cnt


n, m = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

anw = []
cnt_1 = 0
flag = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = bfs(i, j, graph)
            anw.append(cnt)
            cnt_1 += 1
            flag = True
if flag:
    print(cnt_1)
    print(max(anw))
else:
    print(0)
    print(0)



# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end=" ")
#     print()
