from collections import deque

n, m = map(int, input().split())
dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]
# 위치는 (1,1)
# 미로의 출구는 (N, M)의 위치에 존재, 한 번에 한 칸씩 이동
# 괴물이 있는 부분은 0으로, 없는 부분은 1
# 미로는 반드시 탈출할 수 있다.
# 탈출하기 위해 움직여야 하는 최소 칸의 개수

# example
"""
5 6
101010
111111
000001
111111
111111
"""
graph = [list(map(int, input())) for _ in range(n)]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))

    cnt = 1
    while queue:
        a, b= queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1:
                if graph[nx][ny]:
                    graph[nx][ny] = graph[a][b] +1
                    queue.append((nx, ny))
    print(f'cnt : {cnt}')
    return graph[n-1][m-1]

print(bfs(graph, 0,0))