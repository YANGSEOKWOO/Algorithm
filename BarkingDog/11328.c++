#include <iostream>
#include <string>

using namespace std;

string str_arr[1002][2];
int alphabet[26];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    bool flag;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> str_arr[i][0] >> str_arr[i][1];
        fill(alphabet, alphabet + 26, 0);
        flag = true;
        for (int j = 0; j < str_arr[i][0].length(); j++)
        {
            alphabet[str_arr[i][0][j] - 'a']++;
            alphabet[str_arr[i][1][j] - 'a']--;
        }
        for (int i = 0; i < 26; i++)
        {
            if (alphabet[i] != 0)
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            cout << "Possible\n";
        }
        else
        {
            cout << "Impossible\n";
        }
    }
}