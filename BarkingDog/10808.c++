#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int freq[26] = {0};
    string s;
    cin >> s;
    for (auto c : s)
        freq[c - 'a'] += 1;
    for (int i = 0; i < 26; i++)
        cout << freq[i] << ' ';
}