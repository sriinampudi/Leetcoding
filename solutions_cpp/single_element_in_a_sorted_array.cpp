class Solution
{
public:
    int singleNonDuplicate(vector<int> &A)
    {
        if (A.size() == 1)
            return A[0];
        int lo = 0, hi = A.size() - 1;
        int mid = (lo + hi) / 2;
        while (lo < hi - 2)
        {
            if (A[mid] == A[mid + 1])
                mid++;
            if ((hi - mid) % 2)
                lo = mid + 1;
            else
                hi = mid;
            mid = (lo + hi) / 2;
        }
        return A[lo] == A[lo + 1] ? A[hi] : A[lo];
    }
};