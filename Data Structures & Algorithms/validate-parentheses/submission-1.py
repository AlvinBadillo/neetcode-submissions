class Solution:
    def isValid(self, s: str) -> bool:
        # Use a list as a stack
        stack = []
        # Loop through the list
        for char in s:
            # Check if its opening parentheses
            if char == '(' or char == '[' or char == '{':
                # Add it to the stack
                stack.append(char)
            # Else will handle case where its a closing parentheses
            else:
                # If a closing parentheses is the only one in the stack, return false
                if len(stack) == 0:
                    return False
                # Var to hold the previous value
                prevChar= stack.pop()
                if char == ')' and prevChar != '(':
                    return False
                elif char == '}' and prevChar != '{':
                    return False
                elif char == ']' and prevChar != '[':
                    return False
        # Verify that the list is empty at the end of the loop
        if len(stack) == 0:
            return True
        else:
            return False