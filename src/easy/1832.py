class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        return len(set(sentence)) == 26


## Primary Focus: We need to check if all the letters from a-z have occured atleast once or not

## Breaking Down the problem:

# - We don't care if any letter between a-z occurs more than once.
# - So we get only the single occurances of each character in the string by converting it into a set
# which is an ordered sequence of unique elements.
# - Now, we need to check if all the elements between a-z are there. In other words, if our resulting set has all 
#  the 26 letters of English alphabet
# - So we just check if it's length is 26.
