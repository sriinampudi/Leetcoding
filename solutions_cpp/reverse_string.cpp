class Solution {
public:
    void reverseString(vector<char>& s) {
        int start = 0, end = s.size() - 1;    
        
        revStr(s, start, end);
    }
    
    void revStr(vector<char>& s, int start, int end){
        
        if(start >= end) return;
        int temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        
        revStr(s, start+1, end-1);
    }
};