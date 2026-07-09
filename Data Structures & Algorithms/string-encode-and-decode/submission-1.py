class Solution:

    def encode(self, strs: List[str]) -> str:
        # No space, make own delimiter based on length of string 
        result = ""
        for s in strs: 
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        #Break up string into smaller strings according to delimiter 
        #encode each string into an array element

        result = []
        i = 0 

        while i < len(s): 
            #find occurance of #
            hash_pos = s.find('#',i) #find the index position of hash
            length = int(s[i:hash_pos]) # find amount of numbers needed
            word = s[hash_pos+1 : hash_pos + 1 + length]

            result.append(word)
            i = hash_pos + 1 + length
            # grab exactly the manager characters after #
        return result
