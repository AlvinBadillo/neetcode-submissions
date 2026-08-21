class Solution:
    separator = "*@SPACE@*"
    def encode(self, strs: List[str]) -> str:
        # lets define first a separator 
        # start simple *@SPACE@*
        # Now that we have our separator, we can add it in between the each of the strings   
        res = f'{self.separator}'.join(strs)
        print("Encoded string: ", res)
        if len(strs) > 0:
            return res
        else:
            return "#0"


    def decode(self, s: str) -> List[str]:
        if s == "#0":
            return []
        res = []
        curr_word = ""
        # need to detect when the separator is present
        # if it is, we know we have ended the current word
        i = 0
        while i < len(s):
        # for i in range(len(s)):
            # char = s[i]
            flag = True
            # Loop to detect our separator
            for j in range(len(self.separator)):
                # check if separator is posible, if not exit
                if i + len(self.separator) > len(s):
                    flag = False
                    break
                if s[i + j] != self.separator[j]:
                    flag = False
            # Check if we have found the separator
            if flag == True:
                # it means we have found the separator
                # so we want to move i by len(separator) 
                i += len(self.separator)
                # then we add the current word we have to our results list
                res.append(curr_word)
                # then we need to reset the curr_word
                curr_word = ""
            else:
                # if its not a separator, add this letter to our curr word
                curr_word += s[i]
                # Usual skip
                i += 1
        
        # add leftover strings
        res.append(curr_word)
        return res
            

            
