# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1

            key = tuple(key) # key should be immutable
            if key not in groups.keys():
                groups[key] = []

            groups[key].append(s)

        return groups.values()
