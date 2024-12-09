# t 테스트 케이스의 개수
# 가로길이 m, 세로길이 N, 배추가 심어져있는 위치ㄱ의 개수
# K개의 줄(배추의 위치가)가 주어진다.

# 가로길이 : m, 세로길이 : n 만큼의 배열을 만드는 방법
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    bat = [[0]*n for _ in range(m)]
    for j in range(k):
        x, y = map(int, input().split())
        bat[x][y] = 1
    print(bat)

# 내생각
# 1. x가 0, y가 0이라면 세개만 비교가능
# 2. x가 0  y가 0이 아니라면 위에 세개는 비교 안해도 된다.
# 3. x가 0이 아니고 y가 0
