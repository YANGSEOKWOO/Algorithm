# https://www.acmicpc.net/problem/1927
import sys
input = sys.stdin.readline
# x가 자연수라면 배열에 x라는 값을 넣는 연산!!
n = int(input())
heap = []
heap_ptr = 0
def insert(n):
    global heap_ptr
    heap.append(n)
    # idx : 추가한 노드의 위치를 나타낸 것 / 그래서 처음값은 맨끝으로 설정
    idx = heap_ptr
    heap_ptr += 1
    # while 조건 : insert를 한다면 결국 루트까지는 가야한다는 것 
    while idx != 0:
        # 부모와 비교해서 부모보다 크다면 값을 바꾸고
        if heap[idx] < heap[(idx-1)//2]:
            temp = heap[idx]
            heap[idx] = heap[(idx-1)//2]
            heap[(idx-1)//2] = temp
            # idx를 재설정해줌
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
    # length : 배열의 길이 -> 왜냐? 완전이진트리이기 때문에
    #  배열의 길이가 정해진다면 단말노드의 범위가 정해짐
    length = len(heap)
    heap_ptr -= 1
    idx = 0
    while True:
        # 그래서 밑에 if 조건에 따라 idx가 단말노드의 범위 안에 들게된다면 조건을 만족하고 나오게 된다는 것
        if length//2 <= idx < length:
            return ret
        # 자식노드가 왼쪽만 있는 경우임
        if length%2 == 0 and idx == ((length//2)-1):
            if heap[idx] > heap[2*idx +1]:
                temp = heap[idx]
                heap[idx] = heap[2*idx+1]
                heap[2*idx+1] = temp
                idx = 2*idx +1
            else:
                return ret
        else:
            # 왼쪽이 더 큰경우
            if heap[2*idx +1] < heap[2*idx+2]:
                if heap[idx] > heap[2*idx +1]:
                    temp = heap[idx]
                    heap[idx] = heap[2*idx+1]
                    heap[2*idx+1] = temp
                    idx = 2*idx +1
                else:
                    return ret
            else:
                if heap[idx] > heap[2*idx +2]:
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