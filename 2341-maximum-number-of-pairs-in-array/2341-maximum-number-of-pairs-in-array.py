from collections import Counter
class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        res=0
        left=0
        count=Counter(nums)
        for i in count:
            res+=count[i]//2
            left+=count[i]%2
        return [res,left]    
                        


        