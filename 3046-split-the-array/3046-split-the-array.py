from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        countOdd=0
        count=Counter(nums)
        for i in count:           
            if count[i]>2:
                return False 
        return True           

                
            
            
        
            
                
                    
        