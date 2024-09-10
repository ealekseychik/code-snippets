# https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_sum = (len(rolls) + n) * mean - sum(rolls)
        missing_one = missing_sum // n
        if missing_one > 6 or missing_one < 1 or (missing_one == 6 and missing_one * n < missing_sum):
            return []

        diff = missing_sum - missing_one * n
        result = [missing_one] * n
        idx = 0
        while diff > 0:
            prepend = min(6 - missing_one, diff)
            result[idx] += prepend
            diff -= prepend
            idx += 1

        return result
