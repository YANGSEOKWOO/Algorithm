# 도시의 세로 도로=> 모든 정수 x좌표마다 있다.
# 가로도로 => 모든 정수 y좌표마다 있다.

# 1. 도로를 따라서 가로 or 세로로 한블록 움직여서 이번 사거리에서 저 사거리로 움직이는 방법
# 2. 대각선으로 가로지르는 방법

x, y, w, s = map(int, input().split())

max_num = max(x, y)
min_num = min(x, y)
anw = 0
if 2*w < s:
    print((x+y)*w)
elif w < s:
    anw += min_num *s
    anw += (max_num - min_num)*w
    print(anw)
else:
    anw += min_num * s
    anw += ((max_num - min_num)//2) * 2*s
    anw += ((max_num - min_num)%2)*w
    print(anw)
