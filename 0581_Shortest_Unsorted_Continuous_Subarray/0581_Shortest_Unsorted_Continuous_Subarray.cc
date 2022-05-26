#include <vector>
#include <algorithm>

class Solution {
public:
    int findUnsortedSubarray(std::vector<int>& nums) {
        std::vector<int> sorted_nums(nums.size());
        std::copy(nums.begin(), nums.end(), sorted_nums.begin());

        std::sort(sorted_nums.begin(), sorted_nums.end());
        if (nums == sorted_nums) {
            return 0;
        }

        int l = -1;
        int r = -1;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] != sorted_nums[i]) {
                l = i;
                break;
            }
        }

        for (int i = n-1; i >= 0; --i) {
            if (nums[i] != sorted_nums[i]) {
                r = i;
                break;
            }
        }

        return r-l+1;
    }
};