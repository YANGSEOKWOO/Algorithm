from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

r, c, k = map(int, input().split())
# R x C 맵, k : 거리
graph = [[0]*c for i in range(r)]


for i in range(r):
    st = input()
    for j in range(c):
        if st[j] == 'T':
            graph[i][j] = 'T'
# 특정점에서 특정점으로 가는 모든 경우의 수 중 특정 가짓수를 만족하는 것

def bfs(a, b):
    visited = [[False]*c for i in range(r)]
    cnt = 0
    anw = []
    q = deque()
    visited[a][b] = True
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            if 0<= ix < r and 0 <= iy < c and visited[ix][iy] == False:
                if graph[ix][iy] == 0:
                    visited[ix][iy] = True
                    q.append((ix,iy))
                    cnt += 1
            if ix == 0 and iy == c-1:
                anw.append(cnt)
    return anw

an = bfs(r-1,0)
print(an)    

