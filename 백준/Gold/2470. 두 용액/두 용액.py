import math

n = int(input())
sol = sorted(list(map(int, input().split())))

'''
어떻게 하면 최적으로 2개를 짝지을 수 있을까?

그냥 정렬을 
'''

left_side = 0
right_side = n-1

ans = abs(sol[left_side]+sol[right_side])
final = [sol[left_side], sol[right_side]]

while left_side < right_side:
    sum = sol[right_side]+sol[left_side]
    num = abs(sum)
    
    if num < ans:
        ans = num
        final = [sol[left_side], sol[right_side]]
        if ans == 0:
            break
    if sum < 0:
        left_side += 1
    else:
        right_side -= 1
print(final[0], final[1])