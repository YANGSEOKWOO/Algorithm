que = []
def push(n):
    que.append(n)
def pop():
    if que:
        print(que.pop(0))
    else:
        print(-1)

def size():
    print(len(que))

def empty():
    if len(que) == 0:
        print(1)
    else:
        print(0)
        
def front():
    if que:
        print(que[0])
    else:
        print(-1)

def back():
    if que:
        print(que[-1])
    else:
        print(-1)
        
n = int(input())
for i in range(n):
    command = list(input().split())
    if command[0] == "push":
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()

    