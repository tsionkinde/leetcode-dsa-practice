class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count=0
        i=0
        j=0
        for k in range(len(nums)):
            while i<k and nums[k]-nums[i]>2*diff:#2*diff comes from when we silmountaniously solve these 2 equations nums[j] - nums[i] == diff and nums[k] - nums[j] == diff
                i+=1
            while j<k and nums[k]-nums[j]>diff:
                j+=1
            if  i < j < k and  nums[j] - nums[i] == diff  and nums[k] - nums[j] == diff:
                count+=1
        return count        

             

                    
        
                
                

        