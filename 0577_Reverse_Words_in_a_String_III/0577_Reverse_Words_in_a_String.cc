#include <string>

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::string ans = "";
        std::string tmp = "";
        int i = 0;
        int n = s.size();
        
        while (i < n) {
            while (i < n && s[i] != ' ') {
                tmp = s[i] + tmp;
                i += 1;
            }
            ans += tmp + ' ';
            tmp.clear();
            i += 1;
        }
        ans.pop_back();
        return ans;
    }
};