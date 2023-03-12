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

def dfs(v):
    visited[v] = 1
    print(v, end= " ")
    for i in range(1,n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)



# 내 생각의 bfs
# bfs는 어떻게 생긴게 중요함, graph를 어떤식으로 표현했는지
# 보통의 경우 graph를 
# 1. 방문한 것이 필요한 경우
# 2. visited = [] (빈 방문을 만든다.)
# 3. queue = deque([root]) -> 처음 방문하는 애를 기준으로 deque 생성
# 4. while queue:
# 5. 
            