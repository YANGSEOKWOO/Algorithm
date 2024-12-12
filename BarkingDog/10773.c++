#include <iostream>
#include <stack>
using namespace std;

int main()
{
    stack<int> s;
    int k, anw = 0;
    cin >> k;

    for (int i = 0; i < k; i++)
    {
        int num;
        cin >> num;

        if (num == 0)
            s.pop();
        else
            s.push(num);
    }
    while (!s.empty())
    {
        anw += s.top();
        s.pop();
    }
    cout << anw << '\n';
    return 0;
}