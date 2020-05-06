class Solution
{
public:
    int majorityElement(vector<int> &A)
    {
        unordered_map<int, int> map;

        // get input size
        int n = A.size();

        // 1. store each element's frequency in a map
        for (int i = 0; i < n; i++)
        {
            map[A[i]]++;
        }

        // 2. return the element if its count is more than n/2
        for (auto pair : map)
        {
            if (pair.second > n / 2)
            {
                return pair.first;
            }
        }

        // Note that step 2 and step 3 can be merged into one
        /* for (int i = 0; i < n; i++)
	{
		if (++map[A[i]] > n/2)
			return A[i];
	} */

        // return -1 if no majority element is present
        return -1;
    }
};