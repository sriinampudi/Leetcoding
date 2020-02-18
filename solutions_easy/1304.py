# Question 1304
#Given an integer n, return any array containing n unique integers such that they add up to 0.

#Example:

#Input: n = 5
#Output: [-7, -1, 1, 3, 4]
#Explanation: These arrays also are accepted[-5, -1, 1, 2, 3], [-3, -1, 2, -2, 4]


def sumZero(n):
        max_element = n//2
        n_array = []
        if n % 2 != 0:
                n_array.append(0)
        for i in range(1, max_element+1):
                n_array.extend([i, -i])
        return n_array


#Analyzing examples:

#n = 1: ans = [0]
#n = 2: ans = [-1, 1]
#n = 3: ans = [-1, 0, 1]
#n = 4: ans = [-2, -1, 1, 2]
#n = 5: ans = [-2, -1, 0, 1, 2]
#If n is odd, we append 0 to the answer list.
#The maximum value is equal to n//2 and the minimum value is equal to - n//2.


n = int(input("Enter the value of n: "))
print("Possible combination: {}".format(sumZero(n)))
