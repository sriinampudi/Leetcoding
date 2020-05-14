class Solution
{
private:
    void removeOneDigit(string &s)
    {
        for (int i = 0; i < s.length() - 1; i++)
        {
            if (s[i + 1] < s[i])
            {
                s.erase(i, 1);
                return;
            }
        }
        s.erase(s.length() - 1, 1);
    }

public:
    string removeKdigits(string num, int k)
    {
        for (int i = 0; i < k; i++)
        {
            removeOneDigit(num);
        }
        int i = 0;
        while (num[i] == '0')
        {
            num.erase(0, 1);
        }
        if (num.length() == 0)
        {
            return "0";
        }
        return num;
    }
};