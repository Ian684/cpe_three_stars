
#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
    while (b) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test;
    cin >> test;

    while (test--) {
        int n;
        cin >> n;

        vector<vector<int>> cows(n);
        int cycle = 1;

        for (int i = 0; i < n; i++) {
            int t;
            cin >> t;
            cycle = lcm(cycle, t);

            cows[i].resize(t);
            for (int j = 0; j < t; j++) {
                cin >> cows[i][j];
            }
        }

        vector<bool> alive(n, true);
        int remain = n;
        int day = 0;
        int final_day = 0;

        while (true) {
            bool flag = false;

            for (int i = 0; i < cycle; i++) {
                int m = INT_MAX;
                int choose = -1;
                bool find = false;

                for (int cow = 0; cow < n; cow++) {
                    if (!alive[cow]) continue;

                    int value = cows[cow][day % cows[cow].size()];

                    if (value < m) {
                        m = value;
                        choose = cow;
                        find = true;
                    }
                    else if (value == m) {
                        find = false;
                    }
                }

                if (find) {
                    final_day = day + 1;
                    flag = true;
                    alive[choose] = false;
                    remain--;
                }

                day++;

                if (remain == 0) break;
            }

            if (!flag || remain == 0) break;
        }

        cout << remain << " " << final_day << '\n';
    }

    return 0;
}

