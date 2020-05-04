class Solution
{
public:
    int findComplement(int num)
    {
        long ans = 0;
        int binarynum[32];
        int i = 0;
        while (num > 0)
        {
            binarynum[i] = num % 2;
            num = num / 2;
            i++;
        }
        long long p = 2;
        p = pow(p, i);
        for (int j = i - 1; j >= 0; j--)
        {
            p = p / 2;
            if (binarynum[j] == 1)
            {
                binarynum[j] = 0;
            }
            else
            {
                binarynum[j] = 1;
            }
            ans = ans + binarynum[j] * p;
        }
        return ans;
    }
};