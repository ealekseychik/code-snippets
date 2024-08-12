# https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        counter = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                val_lst = [
                    grid[row][col], grid[row][col + 1], grid[row][col + 2],
                    grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2],
                    grid[row + 2][col], grid[row + 2][col + 1], grid[row + 2][col + 2],
                ]
                if len(set(val_lst)) < 9 or val_lst[4] != 5:
                    continue

                if any(x in val_lst for x in (0, 10, 11, 12, 13, 14, 15)):
                    continue

                if val_lst[0] + val_lst[1] + val_lst[2] ==\
                    val_lst[3] + val_lst[4] + val_lst[5] ==\
                    val_lst[6] + val_lst[7] + val_lst[8] ==\
                    val_lst[0] + val_lst[4] + val_lst[8] ==\
                    val_lst[6] + val_lst[4] + val_lst[2] ==\
                    val_lst[0] + val_lst[3] + val_lst[6] ==\
                    val_lst[1] + val_lst[4] + val_lst[7] ==\
                    val_lst[2] + val_lst[5] + val_lst[8]:
                    counter += 1

        return counter
