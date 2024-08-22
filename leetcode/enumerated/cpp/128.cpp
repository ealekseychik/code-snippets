// http://leetcode.com/problems/longest-consecutive-sequence

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::set<int> numset(nums.begin(), nums.end());
        int result = 0;

        for (int i : numset) {
            if (!numset.contains(i - 1)) {
                int current = 1;
                while (numset.contains(i + 1)) {
                    i++;
                    current++;
                }

                result = std::max(current, result);
            }
        }

        return result;
    }
};
