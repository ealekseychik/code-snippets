# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for ch in s.lower():
            if ch.isalnum():
                letters.append(ch)

        return letters == letters[::-1]
