#include <unordered_set>
#include <vector>
#include <algorithm>>
class Solution {
public:
    int longestConsecutive(std::vector<int>& nums) {
        std::unordered_set<int> set(nums.begin(), nums.end());

        int length = 0;
        int max_length = 0;
        int x = 0;
        for (auto n : nums) {
            if (!set.count(n-1)) {
                length = 0;
                x = n;
                while (set.count(x)) {
                    x += 1;
                    length += 1;
                }
                max_length = std::max(length, max_length);
            }
        }
        return max_length;
    }
};