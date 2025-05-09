from collections import deque
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = [list(input()) for _ in range(n)]
graph_eye = copy.deepcopy(graph)
visited = [[False]*n for _ in range(n)]
visited_eye = [[False]*n for _ in range(n)]

def bfs(a, b, color):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny]:
                # 색맹 => R+G, B
                if graph[nx][ny] == color:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return
def bfs_eye(a, b, color):
    queue = deque()
    queue.append((a, b))
    visited_eye[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and not visited_eye[nx][ny]:
                # 색맹 => R+G, B
                if graph_eye[nx][ny] == color:
                    queue.append((nx, ny))
                    visited_eye[nx][ny] = True
    return
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph_eye[i][j] = 'G'
cnt = 0
cnt_eye = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt +=1
            bfs(i, j, graph[i][j])
        if not visited_eye[i][j]:
            cnt_eye +=1
            bfs_eye(i, j, graph_eye[i][j])

print(cnt, cnt_eye)
                
