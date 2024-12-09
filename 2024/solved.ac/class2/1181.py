# import sys
# input = sys.stdin.readline

# n = int(input())
# word = [input() for _ in range(n)]


# # 길이 짧은 순으로 정렬을 어떻게 하지?
# # 1. 1~ n(50)까지 넣는 방법
# anw = []
# for i in range(1, 51):
#     temp = []
#     for j in word:
#         if len(j) == i:
#             temp.append(j)
#     temp = list(set(temp))
#     temp.sort()
#     anw.append(temp)

# for i in anw:
#     for j in i:
#         print(j)

import sys
input = sys.stdin.readline

n = int(input())
words = list(set([input().strip() for _ in range(n)]))
words.sort()
print('\n'.join(sorted(words, key=len)))