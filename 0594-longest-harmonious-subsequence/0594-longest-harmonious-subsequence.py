from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count=Counter(nums)
        the_max=0
        for i in count:
            if i-1 in count:  
                if the_max<count[i]+count[i-1]:
                    the_max=count[i]+count[i-1]

                
                
                
        return the_max      
                

