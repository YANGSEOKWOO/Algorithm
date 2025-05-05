from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False]*100001
value = [0]*100001

def bfs(v,k):
    queue = deque()
    queue.append(v)
    value[v] = 0

    while queue:
        x = queue.popleft()
        if x == k:
            print(value[x])
            return
        back = x-1
        front = x+1
        if x != 0:
            mul = x*2
            if 0<= mul < 100001 and not visited[mul]:
                queue.appendleft(mul)
                value[mul] = value[x]
                visited[mul] = True
        if 0<= back < 100001 and not visited[back]:
            queue.append(back)
            value[back] = value[x] +1
            visited[back] = True
        if 0<= front < 100001 and not visited[front]:
            queue.append(front)
            value[front] = value[x] + 1
            visited[front] = True
        

bfs(n, k)
