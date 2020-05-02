# Question 7
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

def reverse(x):
        result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])
        #Convert the number to a string
        #Reverse it using indexing
        #If the original number is negative ignore the the '-' sign at the beginning of the string
        #Convert the reversed string back to integer
        #Add the sign of the original number
        if -2**31 <= result <= (2**31)-1: #Check if the result is within the desired range
            return result
        else:
            return 0
num = int(input("Enter a number: "))
print("Reversed Number: {}".format(reverse(num)))