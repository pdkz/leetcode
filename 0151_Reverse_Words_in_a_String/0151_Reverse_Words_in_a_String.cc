#include <string>

class Solution {
public:
    std::string reverseWords(std::string s) {
        int n = s.size();
        int i = 0;
        std::string ans = "";
        std::string tmp = "";
        while (i < n) {
            if (s[i] == ' ') {
                i++;
            }
            while (i < n && s[i] != ' ') {
                tmp += s[i];
                i++;
            }
            if (!tmp.empty()) {
                ans = tmp + ' ' + ans;
            }
            tmp.clear();
        }
        ans.pop_back();
        return ans;
    }
};