#include <string>
#include <vector>

using std::invalid_argument;
using std::pair;
using std::string;
using std::to_string;
using std::vector;

class Solution {
public:
    string stringShrink(const string& s) {
        if (s.size() < 1)
            return "";
        
        int counter = 0;
        char startChar = s[0];
        vector<pair<char, int>> dupes;
        for (char ch : s) {
            if (!isalpha(ch))
                throw invalid_argument("String should contain only alphabetical characters");

            if (ch == startChar) {
                counter++;
                continue;
            }

            dupes.push_back({ch, counter});
            counter = 1;
            startChar = ch;
        }

        dupes.push_back({startChar, counter});

        string result;
        for (const auto& dupe : dupes) {
            result += dupe.first;
            if (dupe.second > 1)
                result += to_string(dupe.second);
        }

        return result;
    }
};
