
#include <bits/stdc++.h>
using namespace std;

int main() {
    int test;
    cin >> test;

    for (int t = 0; t < test; t++) {
        int w, n;
        cin >> w >> n;
        w *= 1000;

        set<int> arr;
        double result = 1LL << 32;

        for (int i = 0; i < n; i++) {
            int mn, mx;
            cin >> mn >> mx;

            for (int j = mn; j <= mx; j++) {
                arr.insert(j);
            }

            double temp = 1.0 * mn * mn / (mx - mn);
            result = min(result, temp);
        }

        if (w >= result) {
            cout << 0 << "\n";
        }
        else {
            vector<int> dp(w + 1, 0);

            for (int i : arr) {
                for (int j = i; j <= w; j++) {
                    dp[j] = max(dp[j], dp[j - i] + i);
                }
            }

            cout << w - dp[w] << "\n";
        }

        if (t != test - 1) cout << "\n";
    }

    return 0;
}

