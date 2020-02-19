# Question 728

# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


def selfDividingNumbers(left, right):
    return [x for x in range(left, right+1) if all((i and (x % i == 0) for i in map(int, str(x))))]

left = 1
right = 22
print("Self  Driving Numbers:{}".format(selfDividingNumbers(left,right)))
