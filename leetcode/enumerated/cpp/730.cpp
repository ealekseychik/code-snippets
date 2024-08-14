// https://leetcode.com/problems/k-th-smallest-distance-pair/

#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int low = 0;
        int high = nums.back() - nums.front();

        while (low < high) {
            int mid  = (low + high) / 2;
            int count = 0;
            int left = 0;

            for (int right = 0; right < nums.size(); right++) {
                while (nums[right] - nums[left] > mid) {
                    left++;
                }
                count += right - left;
            }

            if (count >= k)
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }
};
