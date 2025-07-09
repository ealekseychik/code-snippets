// https://leetcode.com/problems/merge-strings-alternately/

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int w1Len = word1.length();
        int w2Len = word2.length();
        int min_len = min(w1Len, w2Len);
        string result;

        for (int i = 0; i < min_len; i++) {
            result += word1[i];
            result += word2[i];
        }
        if (w1Len < w2Len) {
            result += word2.substr(min_len);
        } else {
            result += word1.substr(min_len);
        }
        return result;
    }
};