import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
empty_space = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]
found = False  # 답을 찾았는지 여부

def is_valid(x, y, num):
    # 행 검사
    for i in range(9):
        if graph[x][i] == num:
            return False
    # 열 검사
    for i in range(9):
        if graph[i][y] == num:
            return False
    # 3x3 박스 검사
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if graph[start_x + i][start_y + j] == num:
                return False
    return True

def backtracking(depth):
    global found
    if found:
        return  # 답 찾았으면 더 진행하지 않음

    if depth == len(empty_space):
        for row in graph:
            print(' '.join(map(str, row)))
        found = True
        return

    x, y = empty_space[depth]
    for num in range(1, 10):
        if is_valid(x, y, num):
            graph[x][y] = num
            backtracking(depth + 1)
            graph[x][y] = 0  # 되돌리기 (백트래킹)

backtracking(0)