# https://leetcode.com/problems/line-reflection/

class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        if not points:
            return True
        
        min_x, max_x = float('inf'), float('-inf')
        point_set = set()

        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))

        mid = (min_x + max_x) / 2

        for x, y in points:
            reflect_x = 2 * mid - x
            if (reflect_x, y) not in point_set:
                return False

        return True
