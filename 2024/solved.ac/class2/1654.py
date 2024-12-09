# n 개의 랜선을 만들어야 한다.
# k개의 랜선을 가지고 있다 => 길이가 제각각
# 랜선을 모두 n개의 같은 길이의 랜선으로 만들고 싶다
# k개의 랜선을 잘라서 만들어야 한다.
# n개보다 많이 만들어도 됨
# 만들 수 있는 최대 랜선의 길이!
import sys
input = sys.stdin.readline
k, n = map(int, input().split(" "))

def check_cnt(road_length):
    cnt = 0
    for i in line:
        if road_length == 0:
            return True
        cnt += i//road_length
    if cnt >= n:
        return True
    return False

# 가능하면 크기를 키워
def binary_search(max_num):
    start = 0
    end = max_num

    while start <= end:
        mid = (start + end) //2

        if check_cnt(mid):
            start = mid +1
        else:
            end = mid -1
    return end
line = [int(input()) for _ in range(k)]

max_len = max(line)

anw = binary_search(max_len)
print(anw)
# 여기서 True => 값을 더 올려야 함
# 여기서 False => 값을 더 낮춰야 함
