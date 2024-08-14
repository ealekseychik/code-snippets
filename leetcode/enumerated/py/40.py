# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        while len(candidates) > 0 and candidates[-1] > target:
            candidates.pop()

        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()

        backtrack(0, [], 0)
        return result
