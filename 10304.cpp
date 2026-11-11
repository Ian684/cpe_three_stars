
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        vector<vector<int>> cost(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            cost[i][i] = arr[i];
        }

        for (int l = 2; l <= n; l++) {
            for (int i = 0; i <= n - l; i++) {
                int j = i + l - 1;
                for (int k = i; k <= j; k++) {
                    cost[i][j] += arr[k];
                }
            }
        }

        vector<vector<int>> dp(n, vector<int>(n, 1 << 30));

        for (int i = 0; i < n; i++) {
            dp[i][i] = 0;
        }

        for (int l = 2; l <= n; l++) {
            for (int i = 0; i <= n - l; i++) {
                int j = i + l - 1;

                for (int k = i; k <= j; k++) {
                    if (k == i) {
                        dp[i][j] = min(dp[i][j],
                            dp[k+1][j] + cost[i][j] - arr[k]);
                        continue;
                    }

                    if (k == j) {
                        dp[i][j] = min(dp[i][j],
                            dp[i][k-1] + cost[i][j] - arr[k]);
                        continue;
                    }

                    dp[i][j] = min(dp[i][j],
                        dp[i][k-1] + dp[k+1][j]
                        + cost[i][j] - arr[k]);
                }
            }
        }

        cout << dp[0][n-1] << '\n';
    }

    return 0;
}

