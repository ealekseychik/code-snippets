# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            key = [0] * 26
            for c in item:
                key[ord(c) - ord('a')] += 1

            tkey = tuple(key)
            if tkey not in groups.keys():
                groups[tkey] = []

            groups[tkey].append(item)

        return groups.values()
