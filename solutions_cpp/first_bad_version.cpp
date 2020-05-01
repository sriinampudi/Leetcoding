// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int first = 1;
        int last = n;
        int mid;
        while(first <= last){
            mid = ((last-first)>> 1) + first;
            if(isBadVersion(mid)) last = mid - 1;
            else first = mid + 1;
        }
        return last + 1;

    }
};
