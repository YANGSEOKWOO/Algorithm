n = int(input())
score = list(map(int, input().split(" ")))

m = max(score)

sum_score = 0
# print('m:', m)
for i in score:
    sum_score += (i/m)*100
    # print(f'i : {i}, sum_score: {sum_score}')

print(sum_score/n)