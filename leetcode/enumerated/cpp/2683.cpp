// https://leetcode.com/problems/neighboring-bitwise-xor/
#include <vector>

using std::vector;

class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int XOR = 0;
        for (auto num : derived) {
            XOR = XOR ^ num;
        }
        return XOR == 0;
    }
};
