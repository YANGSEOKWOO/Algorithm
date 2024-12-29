# n : 전체 사람수
# 촌수를 계산해야하는 서로 다른 두 사람의 번호
# m 부모 자식들 간의 관계 개수
import sys
input = sys.stdin.readline

n = int(input())
p_1, p_2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, end, depth):
    visited[start] = 1
    if start == end:
        return True, depth  # 종료 조건에 도달하면 True와 현재 depth 반환

    for i in graph[start]:
        if not visited[i]:
            found, current_depth = dfs(graph, i, end, depth + 1)  # 깊이를 1 증가시켜 전달
            if found:
                return True, current_depth  # True와 찾은 깊이 반환
    return False, depth  # 종료 조건에 도달하지 못하면 False와 현재 depth 반환
found, search_cnt = dfs(graph, p_1, p_2, 0)  # 초기 깊이를 0으로 설정

if found:
    print(search_cnt)  # 탐색 성공 시 깊이 출력
else:
    print(-1)  # 탐색 실패 시 -1 출력