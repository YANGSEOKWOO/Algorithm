# T : 테스트 케이스의 개수
# M, N, K (배추밭의 가로 길이, 세로, 배추가 심어져있는 위치 개수)

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))

    graph[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
    return

for _ in range(T):
    m, n, k = map(int, input().split(" "))
    graph = [[0]*m for i in range(n)]
    
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    anw = 0
    for q in range(n):
        for p in range(m):
            if graph[q][p]:
                bfs(graph, q, p)
                anw +=1
    print(anw)
    
