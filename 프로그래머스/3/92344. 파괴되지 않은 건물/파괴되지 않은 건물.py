# 1 ≤ board의 행의 길이 (= N) ≤ 1,000
# 1 ≤ board의 열의 길이 (= M) ≤ 1,000
# 1 ≤ board의 원소 (각 건물의 내구도) ≤ 1,000
# 1 ≤ skill의 행의 길이 ≤ 250,000


## 단순히 구현하면 1000*1000*2500000 이여서 터진다.
## 어떻게 구현할 수 있을까 

## 구간으로 주어지는데 방법이 있을까 
## 0,0 ,3,4 

## skill을 미리 계산해서 한번에 반영?
## 어떻게?

## 구간별로 어떻게 나눌 수 가 있는거지,,,? 
## 값을 어떻게 저장해야 하는거지 ,,,,
## 가로,세로로 하나 ,,


## [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
## [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]] 


def solution(board, skill):
    answer = 0
    
    c_len = len(board[0])
    r_len = len(board)
    ch = [[0 for _ in range(c_len+1)] for i in range(r_len+1)]
    
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            ch[r1][c1] -= degree
            ch[r1][c2+1] += degree
            ch[r2+1][c1] += degree
            ch[r2+1][c2+1] -= degree            
        else:
            ch[r1][c1] += degree
            ch[r1][c2+1] -= degree
            ch[r2+1][c1] -= degree
            ch[r2+1][c2+1] += degree 
    
   
    
    for i in range(r_len):
        for j in range(c_len):
            ch[i][j+1]= ch[i][j+1]+ch[i][j]
            
    
    for i in range(c_len):
        for j in range(r_len):
            ch[j+1][i] = ch[j+1][i]+ ch[j][i]
    
    
            
    for i in range(r_len):
        for j in range(c_len):
            if ch[i][j] + board[i][j] >0:
                answer+=1 
    
    
   
    return answer