class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_map<char, int> mag;
        for (char x : magazine)
        {
            if (mag.count(x))
            {
                mag[x]++;
            }
            else
            {
                mag[x] = 1;
            }
        }
        for (char x : ransomNote)
        {
            if (mag.count(x))
            {
                mag[x]--;
                if (mag[x] < 0)
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};