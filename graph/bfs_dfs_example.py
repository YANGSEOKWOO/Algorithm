from collections import deque
# dfs

# 인접 노드가 여러개인 경우
# 방문기준을 정해야 함 => 무방향의 경우
# 어떤 요구사항에 따라서 정해야 한다.

# 시작 노드인 1을 스택에 삽입하고 방문처리
# 스택의 최상단 노드인 '1'에 방문하지 않은 인접 노드 '2', '3', '8'
# 이 중 방문기준에 부합하는 노드를 스택에 넣고 방문처리
# 이때 스택의 최상단원소는 2로 바뀜

def dfs(graph,v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    

# bfs
# 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
