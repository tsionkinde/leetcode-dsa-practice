class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        r=len(s)-1
        l=0
        while l<r:
            if s[l]!=s[r]:
                return isPalindrome(l+1,r) or isPalindrome(l,r-1)
                    
            l+=1
            r-=1
        return True          



       
                            
                
                
            
                
                     

        