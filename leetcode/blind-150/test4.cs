// https://leetcode.com/problems/group-anagrams/description/

public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {

        var groups = new Dictionary<string, IList<string>>();
        foreach (string item in strs)
        {
            var sum = new char[26];
            foreach (char c in item)
            {
                sum[c - 'a']++;
            }

            var key = new string(sum);

            if (!groups.ContainsKey(key))
            {
                groups[key] = new List<string>();
            }
            groups[key].Add(item);
        }
        return groups.Values.ToList();
    }
}
