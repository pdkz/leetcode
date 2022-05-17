class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        std::unordered_map<int, int> counter;
        std::sort(nums.begin(), nums.end());

        std::vector<int>::iterator it;
        for (it = nums.begin(); it != nums.end(); ++it) {
            //std::cout << *it << std::endl;
            counter[*it] += 1;
        }

        int n;
        for (it = nums.begin(); it != nums.end(); ++it) {
            if (counter[*it] == 0) {
                continue;
            }

            n = *it;
            counter[n] -= 1;
            for (int i = 1; i < k; ++i) {
                if (counter[n+i] > 0) {
                    counter[n+i] -= 1;
                }
                else {
                    return false;
                }
            }
        }

        return true;
    }
};