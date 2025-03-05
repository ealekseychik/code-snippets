# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vovels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        left, right = 0, len(s_list) - 1
        while left < right:
            while left < right and s_list[left] not in vovels:
                left += 1
            while left < right and s_list[right] not in vovels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)
