# Question 1323
#Given a positive integer num consisting only of digits 6 and 9.
#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6). 

#Example :

#Input: num = 9669

#Output: 9969

#Explanation: 
#Changing the first digit results in 6669.
#Changing the second digit results in 9969.
#Changing the third digit results in 9699.
#Changing the fourth digit results in 9666. 
#The maximum number is 9969.

def maximum69Number (num):
        return int(str(num).replace('6','9',1))

#To obtained the greatest number:
# Firstly, we need to change only 6 to 9 and not vice versa
# Secondly, we need to change only that 6 which is at the highest order of 10 (the first six from the left)

num = int(input("Enter a number containing only 6's and 9's :"))
print("Maximum number you can get by changing at most one digit: {}".format(maximum69Number(num)))
