# Credits: https://github.com/sriinampudi

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if len(str(i))%2 == 0:
                c = c+1
        return(c)
        
#incrementing flag value if len is even