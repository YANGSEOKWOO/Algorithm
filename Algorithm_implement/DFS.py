def dfs_list(graph, start_node):
    # 기본은 항상 두 개의 리스트를 별도로 관리
    need_visited, visited = list(), list()

    # 시작 노드 시정
    need_visited.append(start_node)

    # 아직도 방문이 필요한 노드가 있다면!
    while need_visited:

        # 그 중에 가장 마지막 데이터 추출(스택구조)
        node = need_visited.pop()

        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            
            #방문한 목록에 추가
            visited.append(node)

            # 그노드에 연결된 노드를
            need_visited.extend(graph[node])
    return visited


def dfs_deque(graph, start_node):
    from collections import deque
    visited = []
    need_visited = deque()

    # 시작노드 설정
    need_visited.append(start_node)

    # 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        # 시작노드 시정
        node = need_visited.pop()

        # 만약 방문한 리스트에 없다면
        if node not in visited:
            # 방문리스트에 노드를 추가
            visited.append(node)
            # 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
    return visited

def dfs_recur(graph, start, visited= []):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recur(graph, node, visited)
    return visited

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs_deque(graph, 'A'))