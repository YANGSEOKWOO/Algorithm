import heapq

n = int(input())
heap= []
num = list(map(int, input().split()))
t= 1

for i in range(n):
    heapq.heappush(heap, num[i])
    a = len(heap)
    print(heap)
    if i == (3*t+1):
        print(heap[a//3], heap[(2*a)//3])
    
    
# 정렬을 힙정렬을 하면 된다!
