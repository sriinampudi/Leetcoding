# Question 1021

# A valid parentheses string is either empty(""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.


# Example:

# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

def removeOuterParentheses(S):
                count = 0
                l = []
                start_index = 0
                for i in range(len(S)):
                        if S[i] == '(':
                               count += 1
                        elif S[i] == ")":
                               count -= 1
                        if count == 0:
                               l.append(S[start_index+1:i])
                               start_index = i+1
                return "".join(l)

para_s=input("Enter a string having only paranthesis: ")
print("String after removing outermost paranthesis:{}".format(removeOuterParentheses(para_s)))

