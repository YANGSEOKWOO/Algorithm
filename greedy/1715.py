import sys
from queue import PriorityQueue
input =sys.stdin.readline

n = int(input())

num = PriorityQueue()
for i in range(n):
    num.put(int(input()))
# n = 3 -> 2번반복
anw = 0
for j in range(n-1):
    temp = num.get() + num.get()
    num.put(temp)
    anw += temp
print(anw)