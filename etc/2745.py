import sys
input = sys.stdin.readline
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num, b = input().split()
num = num[::-1]
anw = 0
for i in range(len(num)):
    anw += alphabet.find(num[i])*(int(b)**i)
print(anw)