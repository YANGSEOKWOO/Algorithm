#include <iostream>
#include <vector>

using namespace std;
int func2(const vector<int> &arr, int N);
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << func2({1, 52, 48}, 3);
    cout << func2({50, 42}, 2);
    cout << func2({4, 13, 63, 87}, 4);
}

int func2(const vector<int> &arr, int N)
{
    vector<int> v1(101);
    for (int i = 0; i < N; i++)
    {
        if (v1[100 - arr[i]] == 1)
        {
            return 1;
        }
        else
        {
            v1[arr[i]] += 1;
        }
    }
    return 0;
}