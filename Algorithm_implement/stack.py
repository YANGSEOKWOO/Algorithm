# https://www.acmicpc.net/problem/10828

# empty(stack) -> 스택이 비어있는 경우 1, 그렇지 않으면 0
# push(stack, data) -> 스택에 데이터 저장
# pop(stack) -> 마지막에 저장된 요소를 삭제 및 반환
# peek(stack) -> 마지막에 저장된 요소를 반환, 삭제X


# 1. implement by Arr
class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        if len(self.stack) == 0:
            return 1
        return 0
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) == 0:
            print("스택이 비어있습니다.")
        else:
            return self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            print("스택이 비어있습니다.")
        else:
            return self.stack[-1]
    def print(self):
        print(self.stack)

stack = Stack()
stack.push(100)
stack.print()
stack.push(200)
stack.print()
print(stack.pop())
stack.print()
print(stack.peek())
stack.print()
stack.push(100)
print(stack.empty())


# 2. implement by Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    def append(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)
