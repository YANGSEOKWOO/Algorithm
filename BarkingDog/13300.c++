#include <iostream>

using namespace std;

// 각 성별(S: 0, 1)과 학년(Y: 1~6)에 따라 필요한 방의 개수를 계산합니다.
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k, anw = 0;
    cin >> n >> k;

    // 학생 분류를 위한 배열 (성별 2개 × 학년 6개)
    int member[2][7] = {0}; // 배열 초기화

    // 입력 처리
    for (int i = 0; i < n; i++)
    {
        int s, y;
        cin >> s >> y;
        member[s][y]++;
    }

    // 필요한 방의 개수 계산
    for (int s = 0; s < 2; s++)
        for (int y = 1; y <= 6; y++)
            // 인원이 있다면 필요한 방 개수 추가
            anw += (member[s][y] + k - 1) / k;

    // 결과 출력
    cout << anw << '\n';
    return 0;
}