# Question 1281

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Example

#Input: n = 234

#Output: 15

#Explanation:
#Product of digits = 2 * 3 * 4 = 24
#Sum of digits = 2 + 3 + 4 = 9
#Result = 24 - 9 = 15

import numpy as np
def subtractProductAndSum(n):
   return (lambda n: np.prod(n) - sum(n))(list(map(int, str(n))))
   # str(n) --> Converts n to string
   # int(n) --> Converts n to integer
   # (map(int, str(n)) --> Performs int() on each element of the string obtained by str(n)
   # list(map(int, str(n))) --> Stores the digits of the number in a list
   # sum(n) --> Calculates the sum of the elements of a list
   # np.prod(n) --> Calculates the product of the elements of a list(defined in numpy)
   # lambda n: np.prod(n) - sum(n) -->Lambda Function to find subtract the Product and Sum of Elements of the number

num = int(input("Enter a number: "))
print("The difference of product and sum of digits of the number is: {}".format(subtractProductAndSum(num)))
