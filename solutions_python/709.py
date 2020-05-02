# Question 709
 #Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

#Example 1:

#Input: "Hello"
#Output: "hello"

def toLowerCase(word):
    return word.lower()

word = input("Enter a string: ")
print("Lower Case: {}".format(toLowerCase(word)))

