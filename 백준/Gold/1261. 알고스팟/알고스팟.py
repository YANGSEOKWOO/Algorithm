from collections import deque
dx= [1, -1, 0, 0]
dy= [0, 0, 1, -1]


m, n = map(int, input().split())

graph = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
rock= [[1e9]*m for _ in range(n)]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    rock[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 벽이라면, 부셔
                if graph[nx][ny] == '1':
                    rock[nx][ny] = min(rock[nx][ny], rock[x][y]) + 1
                    queue.append((nx, ny))
                else:
                    rock[nx][ny] = min(rock[nx][ny], rock[x][y])
                    queue.appendleft((nx, ny))
                visited[nx][ny] = True

bfs(0,0)
print(rock[n-1][m-1])

# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=" ")
#         print()
# print_matrix(rock)