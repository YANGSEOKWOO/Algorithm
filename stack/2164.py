from collections import deque
'''
while 카드가 한장 남을때 까지
    제일 위에 있는 카드를 바닥에 버린다.
    제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
'''
n = int(input())
queue = deque([i for i in range(1,n+1)])

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])