class Solution:
    def isValid(self, s: str) -> bool:
        # If string is only one character, we can instantly return False
        if len(s) == 1:
            return False
        # Declare stack
        my_stack = []
        for paren in s:
            # Check what type of paren it is 
            if paren == '(' or paren == '[' or paren == '{':
                # If its an opening one, push it to the stack
                
                my_stack.append(paren)
            else:
                if len(my_stack) == 0:
                    return False
                # If its closed, we need to make sure which one it is
                if paren == ')':
                   
                    # If past paren is not ( we return false
                    if my_stack.pop() != '(':
                        return False
                elif paren == ']':
                    
                    # If past paren is not ( we return false
                    if my_stack.pop() != '[':
                        return False
                elif paren == '}':
             
                    # If past paren is not ( we return false
                    if my_stack.pop() != '{':
                        return False
        # Now check if stack is empty, if it is return True
        # If not, it means there are brackets still open, we return false
        if len(my_stack) == 0:
            return True
        else:
            return False