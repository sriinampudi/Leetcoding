class Solution
{
public:
    int numMatchingSubseq(const string &S, vector<string> &words)
    {
        int ans = 0;
        unordered_map<string, bool> m;
        for (const string &word : words)
        {
            auto it = m.find(word);
            if (it == m.end())
            {
                bool match = isMatch(word, S);
                ans += m[word] = match;
            }
            else
            {
                ans += it->second;
            }
        }
        return ans;
    }

private:
    bool isMatch(const string &word, const string &S)
    {
        int start = 0;
        for (const char c : word)
        {
            bool found = false;
            for (int i = start; i < S.length(); ++i)
                if (S[i] == c)
                {
                    found = true;
                    start = i + 1;
                    break;
                }
            if (!found)
                return false;
        }
        return true;
    }
};