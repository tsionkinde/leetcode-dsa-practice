class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first={}
        count=-1
        for i in range(len(s)):
            if s[i] in first:
                count=max(count,i-first[s[i]]-1)
            else:
                first[s[i]]=i #to put the characters with their index in the dictionary
        return count            
                   

                
                



        