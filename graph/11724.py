from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visit = [0] *(n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 1
    while queue:
        q = queue.popleft()
        for i in range(1,n+1):
            if graph[q][i] == 1 and visit[i] == 0:
                queue.append(i)
                visit[i] = 1
cnt = 0
for i in range(1,n+1):
    if visit[i] == 0:
        bfs(i)
        cnt +=1
print(cnt)