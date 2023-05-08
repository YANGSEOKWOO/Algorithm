#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> arr;
    int ai, bi;
    for (int i = 0; i < n; i++) {
        cin >> ai >> bi;
        arr.push_back({ai, bi});
    }

    vector<pair<int, int>> dp(n, {0, 0});
    dp[0].0 = arr[0].0;
    dp[0].1 = arr[0].1;
    for (int i = 1; i < n; i++) {
        dp[i].0 = max(dp[i - 1].0 + abs(arr[i].1 - arr[i - 1].1), dp[i - 1].1 + abs(arr[i].1 - arr[i - 1].0)) + arr[i].0;
        dp[i].1 = max(dp[i - 1].0 + abs(arr[i].0 - arr[i - 1].1), dp[i - 1].1 + abs(arr[i].0 - arr[i - 1].0)) + arr[i].1;
    }

    cout << max(dp[n - 1].0, dp[n - 1].1) << endl;

    return 0;
}