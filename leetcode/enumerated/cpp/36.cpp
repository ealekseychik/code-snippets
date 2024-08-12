// https://leetcode.com/problems/valid-sudoku/

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9), cols(9), boxes(9);

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.')
                    continue;

                if (rows[r].find(board[r][c]) != rows[r].end() ||
                    cols[c].find(board[r][c]) != cols[c].end() ||
                    boxes[(r / 3) * 3 + c / 3].find(board[r][c]) != boxes[(r / 3) * 3 + c / 3].end()) {
                    return false;
                } else {
                    rows[r].insert(board[r][c]);
                    cols[c].insert(board[r][c]);
                    boxes[(r / 3) * 3 + c / 3].insert(board[r][c]);
                }
            }
        }

        return true;
    }
};
