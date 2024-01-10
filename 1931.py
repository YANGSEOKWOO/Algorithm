# 회의가 곂치지 않게
# 회의실을 사용할 수 있는 회의의 최대 개수
# 회의는 중간에 중단 X
# 한 회의가 끝난 것과 동시에 다음 회의가 시작될 수 있다.

# 1개의 회의실
# 2초
# n개의 회의 (100,000)

import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting = sorted(meeting, key = lambda x : (x[1], x[0]))
# 작업이 빨리 끝나는 애 넣기
# 그 이후를 확인한 후에 끝나는 게 짧은애를 넣는다.
cnt = 0
last = 0
for i in range(n):
    if last <= meeting[i][0]:
        cnt += 1
        last = meeting[i][1]

print(cnt)