// https://leetcode.com/problems/two-sum/description/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var collect = new Dictionary<int, int>();
        for (int i = 0; i <= nums.Length; i++)
        {
            var diff = target - nums[i];
            if (collect.ContainsKey(diff))
                return new int[] {collect[diff], i};
            collect[nums[i]] = i;;
        }

        return new int[] {0, 0};
    }
}
