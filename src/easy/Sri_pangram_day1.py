class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = 0
        for i in range (0,26):
            if(ascii_lowercase[i] not in sentence):
                c = c+1
        
        if (c != 0):
            return(bool(False))
        else:
            return(bool(True))
        
        
'''run a for loop for i = 0 to 26
acsii_lowercase converts the int to ascii
it check if any alphabet from a to z is in the sentance 
if alphabet is not in the sentence the count flag is incremented
the value of count flag is net checked to returen flase or true 
'''
