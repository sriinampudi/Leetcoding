class Solution
{
public:
    bool isPerfectSquare(int num)
    {
        long double sr = sqrt(num);

        // If square root is an integer
        return ((sr - floor(sr)) == 0);
    }
};