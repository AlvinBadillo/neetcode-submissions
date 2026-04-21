class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                # Each sorted word will be the key of a list of all the words
        # Sort each word and add the original word to the value of that key (list of words)
        my_dict = dict()

        for word in strs:
            sorted_string = str(sorted(word))

            if sorted_string in my_dict:
                # add str to list of string in the value of key sorted_string
                my_dict[sorted_string].append(word)
            else:
                # Initialize the list with str in it
                my_dict[sorted_string] = [word]
        # Create list with all of the values
        result = []
        for value in my_dict.values():
            result.append(value)
        return result