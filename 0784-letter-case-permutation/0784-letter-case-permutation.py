class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res=[s]
        for i in range(len(s)):
            if s[i].isalpha():
                temp = []
                for word in res:
                    temp.append(word[:i] + word[i].swapcase() + word[i+1:])
                res.extend(temp)
                
                
        return res   