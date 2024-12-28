from collections import deque
import sys

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [-1]*(f+1)
flag = False
def bfs(v,up, down):
    global flag
    queue = deque()
    queue.append(v)
    visited[v] = 0
    while queue:
        x = queue.popleft()
        if x == g:
            return visited[x]
        for i in (x+up, x-down):
            if 1<= i < f+1 and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[x] +1
    return -1

result = bfs(s, u, d)
if result != -1:
    print(result)
else:
    print("use the stairs")