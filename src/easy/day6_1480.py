# Credits: https://github.com/sriinampudi
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c = 0
        op =[]
        for i in nums:
            c = c+i
            op.append(c)
            
        return(op)