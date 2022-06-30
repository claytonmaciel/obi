#include <bits/stdc++.h>

using namespace std;
const int maxn = 5e5 + 10;
int n, k;
int v[maxn], pref[maxn];

int main() {
	ios::sync_with_stdio(false), cin.tie(0); 
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> v[i];
	}

	pref[1] = v[1]; 
	for (int i = 2; i <= n; i++) {
		pref[i] = pref[i-1] + v[i];
	}
	
	long long ans = 0; // LONG LONG
	for (int i = 1; i <= n; i++) {
		int resp = upper_bound(pref+i, pref+n+1, pref[i-1] + k) - lower_bound(pref+i, pref+n+1, pref[i-1] + k);
		ans += resp;
	}
	cout << ans << "\n";
	return 0;
}