#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

bool compare(const string& a, const string& b) {
	if (a.size() != b.size()) {
		return a.size() < b.size();
	}
	else return a < b;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n;
	cin >> n;
	string s[20000];
	for (int i = 0; i < n; i++) {
		cin >> s[i];
	}
	sort(s, s + n, compare);
	cout << s[0] << "\n";
	for (int i = 1; i < n; i++) {
		if(s[i]!=s[i-1])
			cout << s[i] << "\n";
	}
}