def down_1():
    global cur_cursor
    if cur_cursor == n-1:
        return
    cur_cursor += 1
    return

def up_2():
    return

def c_down_3():
    return

def c_up_4():
    global cur_cursor
    global channels
    if cur_cursor > 0:  # 이동 가능한 경우
        temp = channels[cur_cursor]
        channels[cur_cursor] = channels[cur_cursor-1]
        channels[cur_cursor-1] = temp
        cur_cursor -= 1  # 커서를 위로 이동

n = int(input())
channels = [input() for _ in range(n)]

cur_cursor = 0
cursor = channels.index("KBS1")

# KBS1을 맨 앞으로 이동
for i in range(cur_cursor, cursor):
    print('1', end="")
cur_cursor = cursor
for i in range(cur_cursor, 0, -1):
    print('4', end='')
    c_up_4()
cur_cursor = 0

cursor = channels.index("KBS2")

# KBS2를 맨 앞으로 이동
for i in range(cur_cursor, cursor):
    print('1', end="")
cur_cursor = cursor
for i in range(cur_cursor, 1, -1):
    print('4', end='')
    c_up_4()