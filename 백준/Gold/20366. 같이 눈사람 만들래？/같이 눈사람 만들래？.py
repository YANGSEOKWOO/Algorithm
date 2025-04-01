import sys
input = sys.stdin.readline
import math

n = int(input())
snow_list = sorted(list(map(int, input().split())))

min_anw = 1e9
for i in range(n-1):
    for j in range(i+1, n):
        compare = snow_list[i] + snow_list[j]
        left_side = i+1
        right_side = n-1
        while (left_side < right_side):
            if (right_side == j or right_side == i):
                right_side -=1
                continue
            if (left_side == j or left_side == i):
                left_side +=1
                continue
            temp = snow_list[left_side] + snow_list[right_side]
            min_anw = min(min_anw, abs(compare-temp))

            if (temp < compare):
                left_side +=1
            elif (temp > compare):
                right_side -=1
            else:
                min_anw = 0
                break
            
        

print(min_anw)