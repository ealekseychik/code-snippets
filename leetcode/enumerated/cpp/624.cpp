// https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int min = arrays[0][0];
        int max = arrays[0].back();
        int max_dist {};
        for (int i = 1; i < arrays.size(); i++) {
            max_dist = std::max({max_dist, abs(max - arrays[i][0]), abs(min - arrays[i].back())});
            min = std::min(min, arrays[i][0]);
            max = std::max(max, arrays[i].back());
        }
        return max_dist;
    }
};
