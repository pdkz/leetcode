import java.util.HashMap;
import java.util.Arrays;
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int complement;
        int len = numbers.length;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0;i<len;i++) {
            complement = target - numbers[i];
            if (map.containsKey(complement)) {
                int[] ans = {i+1, map.get(complement)+1};
                Arrays.sort(ans);
                return ans;
            }
            map.put(numbers[i], i);
        }
        throw new IllegalStateException();
    }
}