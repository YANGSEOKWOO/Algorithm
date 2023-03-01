import sys
input = sys.stdin.readline
n = int(input())
arr = []
ptr_idx = 0

def insert(num, ptr, idx):
    arr.append(num)
    while idx != 0:
        if arr[(idx-1)//2] > arr[idx]:
            temp = arr[idx]
            arr[idx] = arr[(idx-1)//2]
            arr[(idx-1)//2] = temp
            idx = (idx-1)//2
        else:
            break
    ptr +=1
    return ptr

def delete(ptr):
    if not arr:
        print(0)
    else:
        print(arr.pop(0))
    return ptr

        


for _ in range(n):
    inp = int(input())
    if inp == 0:
        ptr_idx = delete(ptr_idx)
    else:
        ptr_idx = insert(inp, ptr_idx, ptr_idx)