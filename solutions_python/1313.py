# Problem 1313

#Consider each adjacent pair of elements[a, b] = [nums[2*i], nums[2*i+1]](with i >= 0).  
# For each such pair, there are a elements with value b in the decompressed list.
#Return the decompressed list.

#Example:

#Input: nums = [1, 2, 3, 4]
#Output: [2, 4, 4, 4]
#Explanation: The first pair[1, 2] means we have freq = 1 and val = 2 so we generate the array[2].
#The second pair[3, 4] means we have freq = 3 and val = 4 so we generate[4, 4, 4].
#At the end the concatenation[2] + [4, 4, 4, 4] is [2, 4, 4, 4].

#Solution:
def decompressRLElist(nums):
        decompressed_list = []
        for index in range(len(nums)):
                if index%2==0: #Since for every pair the first number is the frequency and the next one is the value
                               #Hence if scan the list for indices of 0,2,4.. to compute over the pairs (0,1),(2,3)(4,5)...
                        temp = [nums[index+1]]*nums[index] #the value is made into a list and concatenated frequency times with itself
                        decompressed_list.extend(temp) #Since we want all the pairs to be present as elements of a single list,
                                                        #extend function is used instead of append
        return decompressed_list

nums = [1, 2, 3, 4]
print("Decompressed list: {}".format(decompressRLElist(nums)))
