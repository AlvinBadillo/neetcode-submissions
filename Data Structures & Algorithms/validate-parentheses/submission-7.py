class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()

        # Rules:
        # if stack is empty, the next item added has to be an opener
        # If we have a closer, we must pop from the stack and if its the correct opener for that one continue
        # if not return false

        for char in s:
            # First check what the current char is
            if char == ")":
                if len(stack) == 0:
                    return False
                # if we have a closer we need to pop from the stack and it must match the one we currently have
                if stack.pop() != "(":
                    return False
            elif char == "]":
                if len(stack) == 0:
                    return False
                if stack.pop() != "[":
                    return False
            elif char == "}":
                if len(stack) == 0:
                    return False
                if stack.pop() != "{":
                    return False
            # Now on to the openerss, i think we just push it to the stack
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False

            
