# 문자열 S, T
# S -> T 바꾸는

'''
연산
1. 문자열의 뒤에 A추가
2. 문자열의 뒤에 B추가 후 문자열 뒤집기

안되는 조건을 찾는 것이 중요해 보임
간단하게 생각해보면, 시행횟수 t길이 - s길이

'''
import sys

s = list(input())
t = list(input())
flag= False
def dfs(t):
    global flag
    if t == s:
        print(1)
        flag = True
        sys.exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])
dfs(t)
if not flag:
    print(0)