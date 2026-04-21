class Solution:
    # Encode will have a number(length of curr str) and a # before every word
    # This will let me separate them into the original words
    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            result += str(len(word)) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        # First need to find the length of the word
        # Then find the start and ending indexes of the word
        # Then update to the next starting point of next word
        # Ex: '4#tree2#to3#fry'
        result = []
        i = 0
        while(i < len(s)):
            # Find index of next #
            index_of_del = s.index('#', i)
            # Find length of word from i to index_of_del
            len_word = int(s[i : index_of_del])
            # Add word to result 
            result.append(s[index_of_del + 1 : index_of_del + 1 + len_word])
            # Update indexes
            i = index_of_del + len_word + 1
        return result
