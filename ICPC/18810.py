# 여러타입의 스시

# 먹을 수 있는 스시의 전체 피스의 숫자 범위
# 스시를 분배하는 방법 거의 공평하게, 못먹는 스시가 없도록
# 각 타입마다 반을 먹고싶어함
# 홀수가 있다면, 한명이 추가피스를 먹음


# 입력
# 1. 초밥의 타입 수 n
# 2. 마리가 먹을 수 있는 초밥 피스의 수 x1 y1, 최소 x1피스, 최대 y1개의 피스를 먹을 수 있다.
# 3. 마티가 먹을 수 있는 것 x2, y2
# 4. n개의 거쳐 스시의 타입이 나타남, 각 m은 이 타입에서 스시피스의 개수를 의미함

# 출력
# 마리와 마티가 적절하게 초밥을 나눌 수 있다면 Yes, 아니면 No

# 추가피스를 먹는 건 상관없을듯

# 

# 1. 많이 먹는 친구 A를 구한다 (마티, 마리 중)
# 2. 각 m 단계에서 홀수라면 더 많은 쪽을 A에게 전달
# 3. 다 끝났을 때 최소치를 못넘긴다면, 최대치를 넘긴다면 실패
# 4. 어떤경우를 고려해야 할까? => 많이 먹는 친구를 어떻게 정할지
  # ex) 최소값은 높은데 최대값이 낮은 친구의 경우 어떻게할거임!?

import sys
import copy
input = sys.stdin.readline

n = int(input())
mari = list(map(int, input().split()))
marty = list(map(int, input().split()))

mari_1 = copy.deepcopy(mari)
marty_1 = copy.deepcopy(marty)

sushi = [int(input()) for _ in range(n)]

def check(big, small):
  for i in sushi:
    if (i%2):
      big[1] -= i//2+1
      big[0] -= i//2+1
      small[1] -= i//2
      small[0] -= i//2
    else:
      big[1] -= i//2
      big[0] -= i//2
      small[1] -= i//2
      small[0] -= i//2
  if (big[0] > 0 or big[1] < 0 or small[0] > 0 or small[1] < 0):
      return False
  else:
      return True

if(check(marty, mari) or check(mari_1, marty_1)):
  print("Yes")
else:
  print("No")