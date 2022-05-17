#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int ans = -1;
        int l = 0;
        int r = height.size() - 1;
        while (l < r) {
            ans = std::max(ans, std::min(height[l], height[r]) * (r-l));
            if (height[l] < height[r]) {
                l += 1;
            }
            else {
                r -= 1;
            }
        }
        return ans;
    }
};