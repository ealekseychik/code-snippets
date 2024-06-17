# https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        max_dist = 0
        prev = -1
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    max_dist = i
                else:
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i

        if seats[n-1] == 0:
            max_dist = max(max_dist, n - 1 - prev)

        return max_dist
        