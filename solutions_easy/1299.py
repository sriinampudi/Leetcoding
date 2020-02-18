# Question 1299

#Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#After doing so, return the array.


#Example:

#Input: arr = [17, 18, 5, 4, 6, 1]
#Output: [18, 6, 6, 6, 1, -1]

def replaceElements(A):
        for i in range(len(A)-2, -1, -1): #Start with the second last element of the list and Travese it backwards
                A[i] = max(A[i], A[i+1]) #Replace each element with the maximum of itself and the next element in the list
        return A[1:]+[-1] #Append -1 to the end of the list

arr = [17,18,5,4,6,1]
print("Result = {}".format(replaceElements(arr)))

