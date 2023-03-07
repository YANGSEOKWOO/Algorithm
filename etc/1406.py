# 1. 커서는 맨뒤에 위치!
import sys
input = sys.stdin.readline
word = list(input().rstrip())
print(word)
cursor = len(word)-1
n = int(input())

for i in range(n):
    command = input().rstrip()
    if command[0] == "P":
        word.insert(cursor+1,command[-1])
        cursor +=1
    elif command[0] == "L":
        if cursor != -1:
            cursor -= 1
    elif command[0] == "D":
        if cursor < len(word):
            cursor += 1
    elif command[0] == "B":
        if cursor != -1:
            word.pop(cursor)
            cursor -=1
for i in word:
    print(i, end="")

# n = int(input())
# for i in range(n):
#     command = input()
#     if command[0] == "P":
#         word = word[:cursor] + command[-1] + word[cursor:]
#         cursor += 1
#     elif command[0] == "L":
#         if cursor != 0:
#             cursor -=1
#     elif command[0] == "D":
#         if cursor < len(word):
#             cursor +=1
#     elif command[0] == "B":
#         if cursor != 0:
#             word = word[:cursor] + word[cursor:]
#             cursor -=1
# print(word)