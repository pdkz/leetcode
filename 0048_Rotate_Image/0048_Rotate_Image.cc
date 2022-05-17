class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int N = matrix.size();
        int lo = 0;
        int hi = N-1;
        int tmp = 0;
        for (int i = 0; i < N; ++i) {
            lo = 0;
            hi = N-1;
            while (lo < hi) {
                tmp = matrix[i][lo];
                matrix[i][lo] = matrix[i][hi];
                matrix[i][hi] = tmp;
                lo += 1;
                hi -= 1;
            }
        }

        for (int i = 0; i < N-1; ++i) {
            for (int j = 0; j < N-i-1; ++j) {
                tmp = matrix[N-1-j][N-1-i];
                matrix[N-1-j][N-1-i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
    }
};