class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
               # Declare hash-map
        hashMap = {}
        # Iterate through strs
        for str in strs:
            # Sort the string to "normalize it"
            sortedStr = "".join(sorted(str)) 
            # See if it is in the hashmap
            if sortedStr in hashMap:
                # If it is, add str to the values of that key
                hashMap[sortedStr].append(str)
            else:
                # If it is not in the hashmap, add a new entry
                hashMap[sortedStr] = [str]
        # Declare list to return
        result = []
        # Add all of the lists to result
        for value in hashMap.values():
            result.append(value)
        # Retrun result
        return result