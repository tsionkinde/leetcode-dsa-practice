class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        count=1
        longest=1       
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                count+=1                              
            else:
                count=1
            longest=max(longest,count)    

               
        return longest         
        