#include <iostream>
#include <vector>
#include <string>

using namespace std;

int num_set[2000001];
int arr[100000];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x, anw = 0;
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> arr[i];
    cin >> x;
    for (int num = 0; num < n; num++)
    {
        int complement = x - arr[num];
        if (complement >= 0 && num_set[complement])
            anw++;
        num_set[arr[num]]++;
    }

    cout << anw << endl;
    return 0;
}