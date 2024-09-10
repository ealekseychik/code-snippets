# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            
            if grid1[r][c] == 0:
                return False

            grid2[r][c] = 0

            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            return up and down and left and right

        sub_islands = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        sub_islands += 1
        
        return sub_islands
