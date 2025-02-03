# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1Len = len(word1)
        w2Len = len(word2)
        maxLen = max(w1Len, w2Len)
        res = ""

        for i in range(maxLen):
            if w1Len > i:
                res += word1[i]
            if w2Len > i:
                res += word2[i]

        return res
