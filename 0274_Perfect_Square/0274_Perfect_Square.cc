#include <limits>
#include <vector>
#include <cmath>

class Solution {
public:
    int numSquares(int n) {
        int INF = std::numeric_limits<int>::max();
        std::vector<int> dp(n+1);
        for (int i = 0; i < dp.size(); ++i) {
            dp[i] = INF;
        }
        dp[0] = 0;
        dp[1] = 1;
        int max_root = static_cast<int>(std::sqrt(n));
        int s = 1;
        for (int a = 2; a < n+1; ++a) {
            for (int x = 1; x < max_root+1; ++x) {
                s = static_cast<int>(std::pow(x, 2.0));
                if (a > s) {
                    dp[a] = std::min(dp[a-s] + 1, dp[a]);
                }
                else if (a == s) {
                    dp[a] = 1;
                }
                else{
                    break;
                }
            }
        }
        return dp[n];
    }
};