# https://www.acmicpc.net/problem/11279
import sys
input = sys.stdin.readline
# x가 자연수라면 배열에 x라는 값을 넣는 연산!!
n = int(input())
heap = []
heap_ptr = 0
def insert(n):
    global heap_ptr
    heap.append(n)
    idx = heap_ptr
    heap_ptr += 1
    while idx != 0:
        if heap[idx] > heap[(idx-1)//2]:
            temp = heap[idx]
            heap[idx] = heap[(idx-1)//2]
            heap[(idx-1)//2] = temp
            idx = (idx-1)//2
        else:
            return
    return

def delete():
    global heap_ptr
    if len(heap) == 0:
        return 0
    if len(heap) == 1:
        heap_ptr -= 1
        a = heap.pop(0)
        return a
    ret = heap[0]
    heap[0] = heap.pop()
    length = len(heap)
    heap_ptr -= 1
    idx = 0
    # idx가 단말노드가 될 때까지!
    while True:
        if length//2 <= idx < length:
            return ret
        # 자식노드가 왼쪽만 있는 경우임
        if length%2 == 0 and idx == ((length//2)-1):
            if heap[idx] < heap[2*idx +1]:
                temp = heap[idx]
                heap[idx] = heap[2*idx+1]
                heap[2*idx+1] = temp
                idx = 2*idx +1
            else:
                return ret
        else:
            # 왼쪽이 더 큰경우
            if heap[2*idx +1] > heap[2*idx+2]:
                if heap[idx] < heap[2*idx +1]:
                    temp = heap[idx]
                    heap[idx] = heap[2*idx+1]
                    heap[2*idx+1] = temp
                    idx = 2*idx +1
                else:
                    return ret
            else:
                if heap[idx] < heap[2*idx +2]:
                    temp = heap[idx]
                    heap[idx] = heap[2*idx+2]
                    heap[2*idx+2] = temp
                    idx = 2*idx +2
                else:
                    return ret
 
for i in range(n):
    k = int(input())
    if k == 0:
        print(delete())
    else:
        insert(k)