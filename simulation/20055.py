# 1: 올리는 위치, 내리는위치에 도달하면 그 즉시 내림
# 로봇은 컨베이어 벨트 위에서 스스로 이동가능
# 로봇을 올리는 위치에 올리거나, 로봇이 어떤 간으로 이동하면 그 칸의 내구도 즉시 1감소

'''
벨트가 각 칸 위에 있는 로봇과 함께 회전

내구도 언제 감소?
- 올리는 위치에 로봇을 올리는 경우
- 로봇이 그 칸에 이동하는 경우

1번 과정을 거치면 무조건 

길이 N 컨베이어 벨트
K : 내구도가 0인 칸의 개수의 임계점
A: 내구도!
'''
from collections import deque

n, k = map(int, input().split())
belt = deque((map(int, input().split())))
len_belt = len(belt)
robot = deque([False]*len(belt))

step = 0

while True:
    step +=1
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = False

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[n-1] = False

    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    if belt.count(0) >= k:
        print(step)
        break