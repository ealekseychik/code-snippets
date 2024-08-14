// https://leetcode.com/problems/combination-sum-ii/
#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        sort(candidates.begin(), candidates.end());

        while (!candidates.empty() && candidates.back() > target) {
            candidates.pop_back();
        }

        vector<int> current_combination;
        backtrack(0, candidates, target, 0, current_combination, result);

        return result;
    }

private:
    void backtrack(int start, const vector<int>& candidates, int target,
                    int current_sum, vector<int>& current_combination,
                    vector<vector<int>>& result) {
        if (current_sum == target) {
            result.push_back(current_combination);
            return;
        }

        if (current_sum > target) {
            return;
        }

        for (int i = start; i < candidates.size(); ++i) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            current_combination.push_back(candidates[i]);
            backtrack(i + 1, candidates, target, current_sum + candidates[i], current_combination, result);
            current_combination.pop_back();
        }
    }
};
