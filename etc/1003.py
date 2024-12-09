import sys
input = sys.stdin.readline

# 모르는 부분 
# fibo 수열을 메모이제이션 해야하는데
# 그 값을 활용할 수는 있어도 아하~


t = int(input())
zero = 0
one = 0

fibo = [0]*(41)
fibo_zero = [0]*(41)
fibo_one = [0]*(41)
  
fibo[0] = 0
fibo[1] = 1
fibo_zero[0] = 1
fibo_one[1] = 1
for i in range(2,41):
  fibo[i] = fibo[i-1] + fibo[i-2]
  fibo_zero[i] = fibo_zero[i-1] + fibo_zero[i-2]
  fibo_one[i] = fibo_one[i-1] + fibo_one[i-2]

# def fibo(n):
#   global zero, one
#   if n == 0:
#     zero +=1
#     return 0
#   elif n == 1:
#     one +=1
#     return 0
#   else:
#     return fibo(n-1) + fibo(n-2)

for _ in range(t):
  n = int(input())
  print(fibo_zero[n], fibo_one[n], end=" ")
  print()
