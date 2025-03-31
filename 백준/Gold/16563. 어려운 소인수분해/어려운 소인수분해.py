import sys
input = sys.stdin.readline

isPrimeList = [True]*5000001
isPrimeList[2] = True
isPrimeList[3] = True
isPreviusNum = [0]*5000001

for i in range(2, int(5000001**0.5)):
    if isPrimeList[i]:
        for j in range(2*i,5000001,i):
            isPrimeList[j] = False
            isPreviusNum[j] = j//i

n = int(input())
numbers = list(map(int, input().split()))

for i in numbers:    
    temp = i
    anw = []
    while isPreviusNum[temp] != 0:
        anw.append(temp//isPreviusNum[temp])
        temp = isPreviusNum[temp]
    anw.append(temp)
    answer = sorted(anw)
    print(*answer)