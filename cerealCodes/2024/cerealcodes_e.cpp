// Credits to Helen

#include <bits/stdc++.h>
using namespace std;

int main() {
    int loops;
    cin >> loops;

    for (int l = 0; l < loops; l++) {
        int n, k;
        cin >> n >> k;

        int count = 0;
        for (int j = 0; j < k; j++) {
            int one, two;
            cin >> one >> two;

            if (abs(one - two) % 2 != 1) {
                count++;
            }
        }
        cout << count << endl;
    }

    return 0;
}
