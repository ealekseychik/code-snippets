// https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        #include <map>
        std::map<int, int> diffs;
        for (int i = 0; i < nums.size(); i++) {
            if (diffs.find(nums[i]) == diffs.end()) {
                diffs[target - nums[i]] = i;
            } else {
                return vector<int>{diffs[nums[i]], i};
            }
        }
    }
};
