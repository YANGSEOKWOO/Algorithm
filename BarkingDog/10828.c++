#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    stack<int> s;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string com;
        cin >> com;
        if (com == "push")
        {
            int num;
            cin >> num;
            s.push(num);
        }
        else if (com == "pop")
        {
            if (s.size() == 0)
                cout << "-1" << '\n';
            else
            {
                cout << s.top() << '\n';
                s.pop();
            }
        }
        else if (com == "size")
        {
            cout << s.size() << '\n';
        }
        else if (com == "empty")
        {
            if (s.size())
                cout << "0" << '\n';
            else
                cout << "1" << '\n';
        }
        else if (com == "top")
        {
            if (s.size())
                cout << s.top() << '\n';

            else
                cout << "-1" << '\n';
        }
    }
    return 0;
}