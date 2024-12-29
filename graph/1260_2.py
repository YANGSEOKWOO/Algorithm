from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())

node = [[]for _ in range(n+1)]
visited= [0]*(n+1)
visited_2= [0]*(n+1)

def dfs(graph, v, visited, anw):
    visited[v] = 1
    anw.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, anw)
    return anw
def bfs(graph, v, visited, anw):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    anw.append(v)
    while queue:
        pot = queue.popleft()
        for i in graph[pot]:
            if not visited[i]:
                queue.append(i)
                anw.append(i)
                visited[i] = 1
    return anw

for i in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
for i in node:
    i.sort()

anw = []
anw_2 = []
dfs_anw = dfs(node, v, visited, anw_2)
bfs_anw = bfs(node, v, visited_2, anw)

for i in dfs_anw:
    print(i, end=' ')
print()
for i in bfs_anw:
    print(i, end=' ')
