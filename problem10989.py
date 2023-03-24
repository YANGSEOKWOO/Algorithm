'''
n = int(input())
arr = []
for i in range(n):
    value = int(input())
    arr = division(arr, value)

print(arr)

def division(arr, value):
    start = 0
    end = len(arr)-1
    a = False
    if len(arr) >=1:
        while(start <= end):
            mid = (start + end)//2
            if value > arr[mid]:
                start = mid+1
            elif value < arr[mid]:
                end = mid -1
            else:
                arr.insert(value,mid)
                a = True
                return arr
        if a == False:
            if value > arr[mid]:
                arr.insert(value,mid+1)
                return arr
            else:
                arr.insert(value,mid-1)
                return arr
    else:
        arr.append(value)
        return arr
'''
# 헷갈린 부분 : 이분탐색을 써야하는 건 알았는데 값의 비교니까 스타트부분을 arr[0] 이런식으로
# 하려고 했는데 사실 start변수 자체를 index로 사용하면 되는 거였음! 
# 그래서 mid값이 아니라 arr[mid] 이런식으로 주면 되는거임!
