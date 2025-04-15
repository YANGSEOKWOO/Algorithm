n, k = map(int, input().split())
hamburger = list(input())
eated = [False]*n

human = 0
for i in range(n):
    if hamburger[i] == "P":
        flag = False

        # 왼쪽 탐색 (i-K ~ i-1)
        for j in range(i - k, i):
            if 0 <= j < n and hamburger[j] == "H" and not eated[j]:
                eated[j] = True
                human += 1
                flag = True
                break

        # 오른쪽 탐색 (i+1 ~ i+K)
        if not flag:
            for j in range(i + 1, i + k + 1):
                if 0 <= j < n and hamburger[j] == "H" and not eated[j]:
                    eated[j] = True
                    human += 1
                    break

print(human)