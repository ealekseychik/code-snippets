// https://leetcode.com/problems/contains-duplicate/description/

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        return nums.Length > nums.ToHashSet().Count();
    }
}