import sys
input = sys.stdin.readline

n = int(input())
student = [list(input().split()) for i in range(n)]

student_sort = sorted(student, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in student_sort:
    print(i[0])