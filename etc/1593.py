# g: 찾고자 하는 단어W의 길이, n: 벽화에서 추출한 문자열의 길이
g, n = map(int, input().split())
w = input()
s = input()

def get_alpha_array(string):
    alpha = [0] * 52
    for ch in string:
        if ch.isupper():
            alpha[ord(ch) - ord('A')] += 1
        else:
            alpha[ord(ch) - ord('a') + 26] += 1
    return alpha
# print(f'n-g = {n-g}')

origin_alpha = get_alpha_array(w)

window_alpha = get_alpha_array(s[:g])
answer = 0

if window_alpha == origin_alpha:
    answer += 1

for i in range(g, n):
    left_char = s[i - g]
    right_char = s[i]

    if left_char.isupper():
        window_alpha[ord(left_char) - ord('A')] -= 1
    else:
        window_alpha[ord(left_char) - ord('a') + 26] -= 1

    if right_char.isupper():
        window_alpha[ord(right_char) - ord('A')] += 1
    else:
        window_alpha[ord(right_char) - ord('a') + 26] += 1

    if window_alpha == origin_alpha:
        answer += 1

print(answer)
    


