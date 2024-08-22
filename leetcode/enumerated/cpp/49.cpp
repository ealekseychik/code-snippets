// https://leetcode.com/problems/group-anagrams/
#include <vector>
#include <string>
#include <array>
#include <unordered_map>

using std::string;
using std::array;
using std::vector;
using std::unordered_map;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;

        unordered_map<array<int, 26>, vector<string>> kvpair;
        for (const auto& str : strs) {
            array<int, 26> key = {0};
            for (auto ch : str) {
                key[ch - 'a']++;
            }

            kvpair[key].push_back(str);
        }

        for (const auto& key : kvpair) {
            result.push_back(key.second);
        }
        return result;
    }
};
