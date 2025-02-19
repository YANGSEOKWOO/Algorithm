import heapq
n = int(input())

heap = []
q = []
for i in range(n):
    item = list(map(int, input().split()))
    if heap:
        for j in item:
            if heap[0] < j:
                heapq.heappush(heap, j)
                heapq.heappop(heap)
    else:
        for j in item:
            heapq.heappush(heap, j)
print(heap[0])