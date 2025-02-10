h, w = map(int, input().split())
height = list(map(int, input().split()))

len_h = len(height)
rain = 0
for i in range(1,len_h-1):
    left_max= max(height[:i])
    right_max= max(height[i:])
    middle_value = min(left_max, right_max)
    if height[i] < middle_value:
        rain += middle_value- height[i]

print(rain)



