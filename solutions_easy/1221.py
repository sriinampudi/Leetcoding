# Problem 1221

#Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#Given a balanced string s split it in the maximum amount of balanced strings.
#Return the maximum amount of splitted balanced strings.

#Example :

#Input: s = "RLRRLLRLRL"
#Output: 4
#Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

#Solution:

def balancedStringSplit(str):
        r_count, l_count, no_of_balanced_strings = 0, 0, 0 #Variables to count the no of R's,no of L's and total number of balanced strings
        for character in str:
            if character == 'R':
                r_count += 1
            else:
                l_count += 1
            if r_count != 0 and r_count == l_count: #As soon as we find the number of R's and L's scanned sequentially are equal
                no_of_balanced_strings += 1 #A balanced string is formed
                r_count, l_count = 0, 0 #Reset the counters for the next balanced string
        return no_of_balanced_strings

str = input("Enter a string made up of R's and L's only :")
print("Number of balanced strings: {}".format(balancedStringSplit(str)))
