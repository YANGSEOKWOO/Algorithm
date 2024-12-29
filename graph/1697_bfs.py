import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [0]*100001

def bfs(v,k):
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            return
        back = x-1
        front = x+1
        mul = x*2
        if 0<= back < 100001 and not visited[back]:
            queue.append(back)
            visited[back] = visited[x] +1
        if 0<= front < 100001 and not visited[front]:
            queue.append(front)
            visited[front] = visited[x] + 1
        if 0<= mul < 100001 and not visited[mul]:
            queue.append(mul)
            visited[mul] = visited[x] +1

bfs(n, k)
