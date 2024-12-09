import sys
from collections import deque

n, m, r= int(input())

graph = [ [] for _ in range(n+1)]

# 입력받는 간선 정보 그래프화
for i in range(m):
    tmpL = list(map(int, input().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])

for i in range(n+1):
    graph[i].sort()

def bfs(graph, r, visited):
    queue = deque([r])
    visited[r] = 1
    count = 2
    while queue:
        r = queue.popleft()

        for i in graph
