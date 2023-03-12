from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

# for i in range(m):
def dfs(v):
    visited[v] = 1
    print(v, end= " ")
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    queue = [v]
    visited_1[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n+1):
            if(graph[v][i] == 1 and visited_1[i]== 0):
                queue.append(i)
                visited_1[i] =1
visited= [0]*(n+1)
visited_1 = [0]*(n+1)

dfs(v)
print()
bfs(v)