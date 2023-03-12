from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 1
    while queue:
        q = queue.popleft()
        for i in range(1,test+1):
            if graph[q][i] == 1 and visit[i] == 0:
                queue.append(i)
                visit[i] = 1

n = int(input())
for i in range(n):
    test = int(input())
    graph = [[0]*(test+1) for i in range(test+1)]
    li = list(map(int, input().split()))
    li.insert(0,0)
    visit = [0]*(test+1)
    for j in range(1,test+1):  
        graph[j][li[j]] = graph[li[j]][j] = 1
    cnt = 0
    for k in range(1,test+1):
        if visit[k] == 0:
            bfs(k)
            cnt += 1
    print(cnt)
