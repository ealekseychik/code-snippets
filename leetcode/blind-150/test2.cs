// https://leetcode.com/problems/valid-anagram/description/

public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        if (s == t) return true;

        var sCount = new Dictionary<char, int>();
        var tCount = new Dictionary<char, int>();
        for (int i = 0; i < s.Length; i++)
        {
            sCount[s[i]] = 1 + (sCount.ContainsKey(s[i]) ? sCount[s[i]] : 0);
            tCount[t[i]] = 1 + (tCount.ContainsKey(t[i]) ? tCount[t[i]] : 0);
        }

        foreach (var skey in sCount.Keys)
        {
            int tnum = tCount.ContainsKey(skey) ? tCount[skey] : 0;
            if (tnum != sCount[skey]) return false;
        }
        return true;
    }
} 
