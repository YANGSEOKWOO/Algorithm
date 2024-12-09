import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

s= input()
isI = False
cnt = 0
anw_cnt = 0
for i in s:
  # print('i :', i, 'cnt : ', cnt, 'isI :', isI, 'anw_cnt :', anw_cnt)
  if isI:
    if i == 'O':
      isI = False
      cnt +=1
    else:
      if cnt == 2*n+1:
        anw_cnt += 1
      else:
        cnt = 1
        isI = True
  else:  
    if i == 'I':
      isI = True
      cnt += 1
    else:
      cnt = 0
  # print('적용 후 ','i :', i, 'cnt : ', cnt, 'isI :', isI, 'anw_cnt :', anw_cnt)
  if cnt == 2*n +1:
    anw_cnt += 1
    cnt -= 2
    # print('정산완료! ','i :', i, 'cnt : ', cnt, 'isI :', isI, 'anw_cnt :', anw_cnt)
  
    
print(anw_cnt)
