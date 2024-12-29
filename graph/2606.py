import sys
input = sys.stdin.readline

n = int(input())
node = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return 


dfs(1)
print(sum(visited) -1)