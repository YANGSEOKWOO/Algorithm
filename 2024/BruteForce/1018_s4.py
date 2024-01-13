import sys
input = sys.stdin.readline

# 1. 그냥 8x8만 체스판이면 된다.
# 2. 
# n: 세로, m : 가로

n, m = map(int, input().split(" "))
chess = [input().rstrip('\n') for _ in range(n)]

def chess_check(graph, x, y ):
    w_cnt = 0
    b_cnt = 0
    w = "W"
    # word : 처음에 떠야하는 글자
    # n_flag = True => word가 나와야 한다는 것
    n_flag = True
    for i in range(x,x+8):
        for j in range(y, y+8):
            if n_flag:
                if graph[i][j] != w:
                    w_cnt += 1
                else:
                    b_cnt +=1
            else:
                if graph[i][j] == w:
                    w_cnt +=1
                else:
                    b_cnt +=1
            n_flag = not n_flag
        n_flag = not n_flag
    return min(w_cnt, b_cnt)

# def chess_min(x,y):
#     w_cnt = chess_check(chess, 'W', x, y)
#     b_cnt = chess_check(chess, 'B', x, y)
#     return min(w_cnt, b_cnt)

# m 가로, n 세로
anw = 64
for i in range(n-7):
    for j in range(m-7):
        anw = min(anw, chess_check(chess, i,j))

print(anw)