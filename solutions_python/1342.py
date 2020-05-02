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


#Solution:
def numberOfSteps(num):
        no_of_steps=0 #Counter for tracking the number of steps required to perform the operation
       
        while num>0: #Perform computation till we reduce num to zero
            
            if num & 1 == 0: #Check if num is an odd number
                #Performing And Operation of the number and one in 1 binary form
                # 101 (say number is 3)
                # 001 (1 in binary form)
                # +
                # ------
                # 001(This is 1 in binary form)
                # -------
                # On similar computation with other numbers we can conclude that on Performing And Operation  of any number with 1
                # If the result is 1->It is an odd number
                # Otherwise it is an even number

                num-=1 #Reduce it by one
            
            else: #If num is an even number
                num//=2 #Divide it by 2
            
            no_of_steps += 1

        return(no_of_steps)

num = int(input("Enter a number: "))
print("Number of steps required to reduce: {}".format(numberOfSteps(num)))
