#include <iostream>
#include <string>
#include <vector>

using namespace std;

int arr[101];
int main()
{
    int n, v, anw = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    cin >> v;

    for (int i = 0; i < n; i++)
        if (arr[i] == v)
            anw++;
    cout << anw;
    return 0;
}