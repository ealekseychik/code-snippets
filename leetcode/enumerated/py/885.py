# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        result = [(rStart, cStart)]
        steps = 1  # Number of steps to move in a given direction
        d = 0  # Index for directions

        while len(result) < rows * cols:
            for _ in range(2):  # We need to change direction twice after moving "steps" times
                for _ in range(steps):
                    rStart += directions[d][0]
                    cStart += directions[d][1]
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append((rStart, cStart))
                d = (d + 1) % 4  # Change direction

            steps += 1  # Increase the step size after two directions

        return result
