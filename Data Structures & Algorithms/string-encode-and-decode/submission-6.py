class Solution:

    # Encode the srtings by having the length followed by a # to separete each word
    # The number will make sure we get all the characters in the word
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            deliminator = str(len(word)) + '#'
            encoded_string += deliminator + word
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        result = []
        # '4#four3#sip'
        # The string will always start with a number followed by a #
        i = 0
        while i < len(s):
            # Find the index of the next #
            j = s.index('#', i)     # s.index('what im looking for', starting point)
            # Extract number that represents size of the string
            # From i to i + j
            length_of_word = int(s[i : j])
            # Extract word, word is from j + 1 to j + length_of_word
            result.append(s[j+1 : j+1+length_of_word])
            # Increment i 
            i = j + 1 + length_of_word
        return result