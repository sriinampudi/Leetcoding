#Question 1342:

#Given a non-negative integer num, return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

#Example:

#Input: num = 14

#Output: 6

#Explanation:

#Step 1) 14 is even; divide by 2 and obtain 7.
#Step 2) 7 is odd; subtract 1 and obtain 6.
#Step 3) 6 is even; divide by 2 and obtain 3.
#Step 4) 3 is odd; subtract 1 and obtain 2.
#Step 5) 2 is even; divide by 2 and obtain 1.
#Step 6) 1 is odd; subtract 1 and obtain 0.


#Faster Solution:

def numberOfSteps(num):
      num_b = bin(num)[2:] #Converting the number to binary. It is 9, then we get 0b1001
      return(len(num_b)+num_b.count('1')-1)


num = int(input("Enter a number: "))
print("Number of steps required to reduce: {}".format(numberOfSteps(num)))
