#include <iostream>
#include <string>
#include <cmath> // ceil() 사용을 위해 추가
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num_set[10] = {}; // 각 숫자의 개수를 저장할 배열
    int num;
    cin >> num;
    string s = to_string(num);

    for (char c : s)
    {
        int digit = c - '0'; // char를 숫자로 변환
        if (digit == 6 || digit == 9)
            num_set[6] += 1; // 6과 9는 같은 그룹으로 처리
        else
            num_set[digit] += 1;
    }

    // 6과 9를 같은 그룹으로 처리 (올림 계산)
    num_set[6] = (num_set[6] + 1) / 2;

    // 가장 많이 사용된 숫자 세트의 개수 찾기
    int max_count = 0;
    for (int count : num_set)
    {
        if (max_count < count)
            max_count = count;
    }

    cout << max_count << '\n'; // 결과 출력
    return 0;
}