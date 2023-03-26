def solution(common):
    last_idx = len(common)
    if (common[1]-common[0]) == (common[2]-common[1]):
        return common[last_idx-1] + (common[1]-common[0])
    return common[last_idx-1]*(common[1]//common[0])

# 1. 공차인걸 확인하는 방법
# common의 길이가 최소 3
