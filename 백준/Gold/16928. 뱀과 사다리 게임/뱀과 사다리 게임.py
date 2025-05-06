# '''
# 사다리 => 
# '''
from collections import deque

# # N: 사다리 수, M; 뱀의 수
# n, m = map(int ,input().split())
# ladder = [list(map(int, input().split())) for _ in range(n)]
# snake = [list(map(int, input().split())) for _ in range(m)]
# dp = [int(1e9)]*101

# def isLadder(index, cur):
#     for start, end in ladder:
#         if index == start:
#             dp[end] = min(dp[end], cur+1)
#             return end
#     return 0

# def isSnake(index, cur):
#     for start, end in snake:
#         if index == start:
#             if dp[end] > cur +1:
#                 dp[end] = cur+1
#                 return end
#     return False

# def bfs(v):
#     cur = 0
#     queue = deque()
#     queue.append((v, cur))

#     while queue:
#         idx, current = queue.popleft()
#         for i in range(1,7):
#             x = idx+i
#             if 0<x<= 100:
#                 ladder_check = isLadder(x, current)
#                 if ladder_check:
#                     queue.append((ladder_check, current+1))
#                 else:
#                     snake_check = isSnake(x, current)
#                     if snake_check:
#                         queue.append((snake_check, current+1))
#                     else:
#                         queue.append((x, current+1))
# bfs(1)
# print(dp)
                

n, m = map(int ,input().split())
ladder = [list(map(int, input().split())) for _ in range(n)]
snake = [list(map(int, input().split())) for _ in range(m)]
visited = [False]*101
dp = [int(1e9)]*101

def isLadder(number):
    global ladder
    for start, end in ladder:
        if number == start:
            # print(f'value:{start}, end:{end}')
            return end
    return 0

def isSnake(number):
    global snake
    for start, end in snake:
        if number == start:
            return end
    return

def bfs():
    queue = deque()
    # 현재위치 , 방문 횟수
    queue.append((1, 0))
    visited[1] = True
    dp[1] = 0

    while queue:
        x, cnt = queue.popleft()

        for i in range(1,7):
            search_idx = x + i

            if search_idx <= 100 and not visited[search_idx]:
                ladder_check = isLadder(search_idx)
                if ladder_check:
                    if visited[ladder_check]:
                        continue
                    queue.append((ladder_check, cnt +1))
                    visited[search_idx] = True
                    dp[search_idx] = cnt +1
                    continue
                snake_check = isSnake(search_idx)
                if snake_check:
                    queue.append((snake_check, cnt+1))
                    visited[search_idx] = True
                    dp[search_idx] = cnt +1
                    continue
                queue.append((search_idx, cnt+1))
                visited[search_idx] = True
                dp[search_idx] = cnt +1                

bfs()
print(dp[100])