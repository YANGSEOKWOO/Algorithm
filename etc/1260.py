# n : 정점의 개수, m : 간선의 개수, v : 정점의 번호
# m개 줄에 간선이 연결하는 두 정점의 번호
# 양방향

from collections import deque
import sys
input = sys.stdin.readline

# def BFS(v):
#     q = deque()
#     q.append(v)
#     visit_list[v] = 1
#     while q:
#         v = q.popleft()
#         print(v, end=" ")
#         for i in range(1,n+1):
#             if visit_list[i] == 0 and graph[v][i] == 1:
#                 q.append(i)
#                 visit_list[i] == 1
def bfs(v):
    q= deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v= q.popleft()
        for i in range(1,n+1):
            if visit_list[i] ==0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i]==1
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
# 모두 큐에 삽입하고 방문 처리
# 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복
n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visit_list = [0] *(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

