import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split(' '))) for _ in range(n)]
INF = 2147000000
res = INF

visited = [False for _ in range(n)]

def DFS(L, idx):
  global res
  if (n//2 == L):
    a = 0
    b = 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          a += graph[i][j]
        elif not visited[i] and not visited[j]:
          b += graph[i][j]
    res = min(res, abs(a-b))
    return
  for i in range(idx, n):
    if not visited[i]:
      visited[i] = True
      DFS(L+1,i+1)
      visited[i] = False
DFS(0,0)
print(res)

# 시간제한 2초
# n : 20까지
# n = 4, 2 / n = 6, 3
# 어려운 점 : n이 4일때는 12, 13, 14, 23, 24, 34를 확인했어야 하는데
# n이 6일때는 경우의 수가 더 많아진다. 순열로 그러면 어떻게 로직을 짤 수 있는지

# 생각했던 방법
# dp인줄 알았음, 그 전 로직 등등... 근데 너무 이상했긴했음
# 입력값에 따라 고려해야하는 가짓수가 팩토리얼만큼 늘어날 때 어떻게 구현을 해야 하는가

# dfs인 이유
# 1. 내가 말했던 것 처럼 입력값에 따라 고려해야 하는 가짓수가 늘어나겠지만, 결국 고려해야 하는 것은
# 2가지의 팀이고, 그 값만 비교하면 되는 거였음


# 알게 된 사실
# 1. 입력값에 따라 고려해야 하는 가짓 수가 늘어난다면 dfs를 고민해 봐야한다.
# 2. 재귀함수를 호출 할 때 여러개가 호출되니까 return에는 아무것도 안넣는게...