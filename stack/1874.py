# 1~n까지의 수를 스택에 넣었
# 첫줄에 n, 둘째줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력. push연산은 +, pop연산은 -
# 불가능한 경우 NO





n = int(input())
import sys
input = sys.stdin.readline

arr = [i for i in range(n+1)]
ptr = 1
flag = False
stack = []
result = []
for i in range(n):
    num = int(input())
    
    while ptr <= num:
        stack.append(ptr)
        result.append("+")
        ptr +=1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = True
        break

if flag:
    print("NO")
else:
    for i in result:
        print(i)
