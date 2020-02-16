# Question 1295

# Given an array nums of integers, return how many of them contain an even number of digits.

# Example

#Input: nums = [12,345,2,6,7896]

#Output: 2

#Explanation:
#12 contains 2 digits(even number of digits).
#345 contains 3 digits(odd number of digits).
#2 contains 1 digit(odd number of digits).
#6 contains 1 digit(odd number of digits).
#7896 contains 4 digits(even number of digits).
#Therefore only 12 and 7896 contain an even number of digits.

#Solution:

def findNumbers(nums):
    return len([num for num in nums if len(str(num))%2 == 0])
    # str(num)--> Convert a number into string
    # len(str(num))--> Find the length of the string
    # if len(str(num))%2==0 --> Check if length of string is divisible by 2
    # for num in nums if len(str(num))%2 == 0] --> Perform it for all the elements in the list 'nums'
    # [num for num in nums if len(str(num))%2 == 0] Store only those elements in a new list whose length is even
    # len([num for num in nums if len(str(num))%2 == 0]) --> find the number of elements in the desired list

nums = [12, 345, 2, 6, 7896]
print("Count of numbers with an even number of digits:{}".format(findNumbers(nums)))
