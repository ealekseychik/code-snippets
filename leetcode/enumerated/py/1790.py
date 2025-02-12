# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        first_swap = None
        second_swap = None
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue

            if second_swap is not None:
                return False

            if first_swap is not None:
                if s1[first_swap] != s2[i] or\
                    s1[i] != s2[first_swap]:
                    return False
                
                second_swap = i
            else:
                first_swap = i

        if not second_swap:
            return first_swap == None

        return True