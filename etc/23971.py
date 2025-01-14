
h, w, n, m = map(int, input().split())
'''
H: 행
W : 행마다 W개씩
M : 가로
N : 세로
'''

# 일단 1,1에 앉는 것이 최적으로 보임
y = 0
x = 0
if h % (n+1) == 0:
    y = h//(n+1)
else:
    y = h//(n+1)+1

if w % (m+1) == 0:
    x = w//(m+1)
else:
    x = w//(m+1) +1

print(x*y)