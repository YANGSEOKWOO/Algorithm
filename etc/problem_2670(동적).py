n = int(input())

nums = [float(input()) for _ in range(n)]
for i in range(1,n):
    nums[i] = max(nums[i-1]*nums[i], nums[i])
print(nums)
# 8개라면
# 1. 8개의 원소들 하나를 봤을 때 최대값
# 2. 2개 연달아서 있는 것 중 최대값 (8-1번) : 7번
# 3. 3개 연달아서 있는것 (8-2번) : 6번
# 4. 4개 연달아서 있는 것 (8-3번) : 5번
# 언제까지? 8개를 연달아서 곱할때 까지 : 1번