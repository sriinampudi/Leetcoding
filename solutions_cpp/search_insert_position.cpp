class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int i = 0, j = nums.size() - 1;
        int mid;
        while (i < j)
        {
            mid = i + (j - i) / 2;
            if (target == nums[mid])
            {
                return mid;
            }
            if (target > nums[mid])
            {
                i = mid + 1;
            }
            else
            {
                j = mid - 1;
            }
        }
        return (target > nums[i]) ? i + 1 : i;
    }
};