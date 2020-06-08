class Solution
{
public:
    bool isPowerOfFour(int num)
    {
        if (num <= 0)
            return false;
        int d = int(log2(num) / log2(4));
        return pow(4, d) == num;
    }
};