import sys
input = sys.stdin.readline

n = int(input())
anw = 1

for i in range(1,n+1):
  anw *= i

str_anw = str(anw)
cnt = 0
for i in range(1,len(str_anw)+1):
  if str_anw[-i] != '0':
    break
  else:
    cnt+=1
print(cnt)
    